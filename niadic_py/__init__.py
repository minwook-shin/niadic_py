"""
# NIADic_Py

Unofficial Python Wrapper for NIADic dataset

# Description

This is Python wrapper for the NIADic provided by the K-ICT Big Data Center.

# Column

* term : korean words
* tag : word class
  * Using [Korean POS tags comparison chart](
https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0)
* category: Category of words

# Tokenizer Example

* input : "우리는 도서관에서 재미있는 책을 읽고 맛있는 급식을 먹었습니다."
* output : ['우리', '도서관', '재미있', '책', '읽', '맛있', '급식', '먹']

# License

'NIADic_py' contains the bundled NIADic files and available under the CC BY-SA 2.0 license.

"""
from niadic_py.services.file_service import FileService
from niadic_py.services.tokenizer_service import TokenizerService

__all__ = ["FileService", "TokenizerService"]
