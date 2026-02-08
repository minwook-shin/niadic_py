from niadic_py.services.file_service import FileService
from niadic_py.services.tokenizer_service import TokenizerService

# 1. Load Data
print(">>> Loading NIADic data...")
file = FileService(file_type="csv", display_max_rows=False)
file.import_file()
print(">>> Data loaded.\n")

# 2. Basic Statistics
print(">>> Data Statistics:")
print(f"Total Terms: {len(file.get_all_column())}")
print(f"Tag Counts (Top 5):\n{file.get_tag_column().value_counts().head(5)}")
print(f"Category Counts (Top 5):\n{file.get_category_column().value_counts().head(5)}\n")

# 3. Search Examples
print(">>> Search Examples:")
# Search for endings (tags starting with 'e')
endings = file.search_tag(keyword="^e", regex=True)
print(f"Found {len(endings)} ending tags. First 3:\n{endings.head(3)}")

# Search for special characters category
special_chars = file.search_category(keyword="special_characters", regex=False)
print(f"Found {len(special_chars)} special character terms. First 3:\n{special_chars.head(3)}\n")

# 4. Enhanced Tokenizer Example
print(">>> Tokenizer Example:")
print("Features: Dictionary-based validation, Particle (josa) removal, Performance optimization")
# Example with various particles (josa) and endings to demonstrate stemming
example = "우리는 도서관에서 재미있는 책을 읽고 맛있는 급식을 먹었습니다."
print(f"Input: '{example}'")

# The tokenizer now uses the dictionary to validate stems before stripping suffixes
tokenizer = TokenizerService(file.get_all_column(), string=example)
tokens = tokenizer.tokenizer()
print(f"Output: {tokens}\n")

# 5. Verify Tokens
print(">>> Token Verification:")
for token in tokens:
    word_info = file.search_term(keyword=rf"^{token}$", case=False, regex=True)
    if not word_info.empty:
        # Display the first match's tag
        print(f"'{token}': Found in dictionary (Tag: {word_info.iloc[0]['tag']})")
    else:
        # Check for lemma (Stem + '다')
        lemma_info = file.search_term(keyword=rf"^{token}다$", case=False, regex=True)
        if not lemma_info.empty:
            print(f"'{token}': Stem found (Lemma: '{token}다', Tag: {lemma_info.iloc[0]['tag']})")
        else:
            print(f"'{token}': Not found in dictionary")
