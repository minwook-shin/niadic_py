"""
NIADic File Service
"""
from pandas import DataFrame, Series
import pandas as pd

from niadic_py.data import CSV_FILE, XLSX_FILE


class FileService:
    """
    NIADic File class

    ```python
    from niadic_py.services.file_service import FileService

    file = FileService(file_type="csv")
    file.import_file()

    file.get_all_column().head(1)
    file.get_tag_column().value_counts()
    file.get_category_column().value_counts()

    # search tag
    ending = file.search_tag(keyword="^e", regex=True)
    # search category
    special_characters = file.search_category(keyword="special_characters", regex=False)
    ```
    """
    def __init__(self, file_type="csv", display_max_rows=False):
        """
        NIADic File init class
        :param file_type: NIADic file type ("csv", "xlsx"), Default Value = csv
        :param display_max_rows: Default Value = False
        """
        self.__file_type: str = file_type  #
        self.__display_max_rows: bool = display_max_rows
        self.__df: DataFrame = DataFrame()

    def import_file(self) -> DataFrame:
        """
        Choose between Excel or CSV file to set up index.
        :return: DataFrame
        """
        if self.__display_max_rows:
            pd.set_option("display.max_rows", None)

        if self.__file_type == "csv":
            self.__df = pd.read_csv(CSV_FILE, low_memory=False)
        elif self.__file_type == "xlsx":
            self.__df = pd.read_excel(XLSX_FILE)
        self.__df.set_index('term', inplace=True)
        return self.__df

    def get_all_column(self) -> DataFrame:
        """
        Query all data in a DataFrame.
        :return: DataFrame
        """
        return self.__df

    def get_term_column(self) -> Series:
        """
        Query term Series in a DataFrame.
        :return: term Series
        """
        return self.__df.index

    def get_tag_column(self) -> Series:
        """
        Query tag Series in a DataFrame.
        :return: tag Series
        """
        return self.__df["tag"]

    def get_category_column(self) -> Series:
        """
        Query category Series in a DataFrame.
        :return: category Series
        """
        return self.__df["category"]

    def search_term(self, keyword: str, case=False, na=None, regex=True) -> DataFrame:
        """
        Search for term data in the DataFrame.
        :param keyword: Character sequence or regular expression.
        :param case: If True, case-sensitive.
        :param na: Fill value for missing values.
        :param regex: If True, assumes the keyword is a regular expression.
        If False, treats the keyword as a literal string.
        :return: term DataFrame
        """
        return self.__df[self.__df.index.str.contains(keyword, case=case, regex=regex, na=na)]

    def search_tag(self, keyword: str, case=False, na=None, regex=True) -> DataFrame:
        """
        Search for search data in the DataFrame.
        :param keyword: Character sequence or regular expression.
        :param case: If True, case-sensitive.
        :param na: Fill value for missing values.
        :param regex: If True, assumes the keyword is a regular expression.
        If False, treats the keyword as a literal string.
        :return: search DataFrame
        """
        return self.__df[self.__df.tag.str.contains(keyword, case=case, regex=regex, na=na)]

    def search_category(self, keyword: str, case=False, na=False, regex=True) -> DataFrame:
        """
        Search for category data in the DataFrame.
        :param keyword: Character sequence or regular expression.
        :param case: If True, case-sensitive.
        :param na: Fill value for missing values.
        :param regex: If True, assumes the keyword is a regular expression.
        If False, treats the keyword as a literal string.
        :return: category DataFrame
        """
        return self.__df[self.__df.category.str.contains(keyword, case=case, regex=regex, na=na)]
