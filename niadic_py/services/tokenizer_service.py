"""
NIADic Tokenizer Service
"""
from typing import List, Set
import re
from pandas import DataFrame


class TokenizerService:
    """
    NIADic Tokenizer class
    .. warning:: This feature is experimental.

    ```python
    from niadic_py.services.tokenizer_service import TokenizerService

    file = FileService(file_type="csv")
    file.import_file()
    example = "저는 오늘 아침에 하나의 빵을 먹고 학교로 급하게 갔습니다."
    token = TokenizerService(file.get_all_column(), string=example).tokenizer()
    ```
    """
    _CLEAN_PATTERN = re.compile(r"[^\uAC00-\uD7A30-9a-zA-Z\s]")

    def __init__(self, df: DataFrame, string: str):
        """
        NIADic Tokenizer init
        :param df: DataFrame containing dictionary data
        :param string: input string
        """
        self._string: str = string
        self._df: DataFrame = df
        self._dictionary_terms: Set[str] = set(self._df.index)
        self._endings: List[str] = self._extract_endings()

    def _extract_endings(self) -> List[str]:
        """
        Extract and sort ending and particle tags from the DataFrame.
        Pre-computation improves performance by avoiding repeated DataFrame filtering.
        """
        # Filter for tags starting with 'e' (endings) or 'j' (particles/josa)
        mask = self._df['tag'].astype(str).str.match(r'^[ej]', case=False)
        endings = self._df.index[mask].unique().tolist()

        # Sort by length in descending order to match longest suffixes first
        endings.sort(key=len, reverse=True)
        return endings

    def _clean_text(self, text: str) -> str:
        """
        Clean up sentences by removing special symbols.
        :param text: input text
        :return: cleaned text
        """
        return self._CLEAN_PATTERN.sub("", text)

    def _process_token(self, text: str) -> str:
        """
        Process a token to find its stem by removing endings/particles recursively.
        Validates the stem against the dictionary.
        Also checks for predicate base forms (stem + '다').
        :param text: word to process
        :return: stem (or base form) if found and valid, otherwise original text
        """
        # 1. If the word itself is in the dictionary, return it.
        if text in self._dictionary_terms:
            return text

        # 2. Check predicate base form (Stem + '다')
        # This handles verbs/adjectives where the dictionary entry ends with '다'
        stem_da = text + "다"
        if stem_da in self._dictionary_terms:
            return text

        # 3. Try to strip endings/particles recursively
        for ending in self._endings:
            if text.endswith(ending):
                stem = text[:-len(ending)]
                if not stem:
                    continue

                # Recursive call to handle multiple suffixes (e.g., 었+습니다)
                found_stem = self._process_token(stem)
                if found_stem in self._dictionary_terms or (found_stem + "다") in self._dictionary_terms:
                    return found_stem

        return text

    def tokenizer(self) -> List[str]:
        """
        Extract meaningful words from given sentence.
        :return: Words list
        """
        cleaned_text = self._clean_text(self._string)
        split_words = cleaned_text.split()
        
        return [self._process_token(word) for word in split_words]
