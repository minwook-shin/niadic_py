"""
NIADic Tokenizer Service
"""
from pandas import DataFrame
import re


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
    def __init__(self, df, string):
        """
        NIADic Tokenizer init
        :param string: input string
        """
        self.__string: str = string
        self.__df: DataFrame = df

    def __clean_text(self):
        """
        Clean up sentences by removing special symbols.
        :return: sentences
        """
        self.string = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", self.__string)
        return self.string

    def __remove_ending(self, text):
        """
        Clean up sentences by removing ending tag.
        :param text:
        :return:
        """
        end_df = self.__df[self.__df.tag.str.contains("^e")]
        index_list = end_df.index.tolist()
        for index in index_list:
            if text.endswith(index):
                text = text[:len(text) - len(index)]
                break
        return text

    def tokenizer(self):
        """
        Extract meaningful words from given sentence.
        :return: Words list
        """
        words_candidate = []
        self.__clean_text()

        split_words = self.string.split()
        for split_word in split_words:
            clear_end = self.__remove_ending(text=split_word)
            words_candidate.append(clear_end)
        return words_candidate
