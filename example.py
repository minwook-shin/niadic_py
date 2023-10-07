from niadic_py.services.file_service import FileService
from niadic_py.services.tokenizer_service import TokenizerService

# setting
file = FileService(file_type="csv", display_max_rows=False)
file.import_file()

# value_counts
print(file.get_all_column().head(1))
print(file.get_tag_column().value_counts())
print(file.get_category_column().value_counts())

# search tag
ending = file.search_tag(keyword="^e", regex=True)
print(ending)

# search category
special_characters = file.search_category(keyword="special_characters", regex=False)
print(special_characters)

# tokenizer
example = "저는 오늘 아침에 하나의 빵을 먹고 학교로 급하게 갔습니다."
token = TokenizerService(file.get_all_column(), string=example).tokenizer()
print(token)

# search term
for i in token:
    word_info = file.search_term(keyword=rf"^{i}$", case=False, regex=True)
    if not word_info.empty:
        print(word_info)
