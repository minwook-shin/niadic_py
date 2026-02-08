# AI Agent Context - Code Changes

## TokenizerService Refactoring

### Summary
Refactored `TokenizerService` to significantly improve performance and code quality.

### Changes
1.  **Performance Optimization**:
    -   **Bottleneck Removal**: Moved the DataFrame filtering logic for extracting "ending" tags from the per-word loop (`tokenizer` -> `_remove_ending`) to the initialization phase (`__init__`).
    -   **Pre-computation**: The list of ending terms is now computed once when the service is instantiated, rather than re-querying the DataFrame for every word in the sentence.
    -   **Greedy Matching**: The ending terms are now sorted by length in descending order. This ensures that the longest matching suffix is removed first, which is logically more correct for tokenization.

2.  **Code Quality & Style**:
    -   **Naming Conventions**: Renamed private methods from double underscore (`__`) to single underscore (`_`) to adhere to Python PEP 8 conventions.
    -   **Type Hinting**: Added Python type hints to methods for better static analysis and readability.
    -   **State Management**: Refactored `_clean_text` to return the modified string instead of mutating the instance attribute `self.string` implicitly.

3.  **Logic**:
    -   Replaced regex-based filtering with `startswith` (where applicable) or optimized logic for better readability.

### Impact
-   Drastic reduction in execution time for `tokenizer()` method due to elimination of repeated DataFrame operations.
-   Improved maintainability and readability for future AI agents and developers.

## Environment Configuration

### Summary
Added `requirements.txt` to resolve `numpy` and `pandas` binary incompatibility.

### Changes
-   **Dependency Management**: Created `requirements.txt` specifying compatible versions of `pandas` and `numpy` (addressing `ValueError: numpy.dtype size changed`).

## TokenizerService Improvement

### Summary
Enhanced `TokenizerService` to utilize the NIADic dictionary for smarter tokenization.

### Changes
-   **Dictionary Validation**: Added `_dictionary_terms` set to validate stems against the dictionary in O(1) time.
-   **Expanded Suffixes**: Updated `_extract_endings` to include particles (tags starting with 'j') alongside endings ('e'), enabling better handling of noun-particle combinations.
-   **Smart Stemming**: Replaced `_remove_ending` with `_process_token`. It now only strips a suffix if the resulting stem exists in the dictionary, preventing over-stemming of unknown words.
-   **Optimization**: Pre-compiled the regex pattern for text cleaning.

## Documentation Update

### Summary
Updated documentation with new Tokenizer examples and results.

### Changes
-   **README & __init__**: Updated the "Tokenizer Example" section to reflect the enhanced tokenizer's behavior with a new sentence and actual output.

## TokenizerService Fix

### Summary
Updated `TokenizerService` to handle Korean predicate base forms.

### Changes
-   **Predicate Handling**: In `_process_token`, if the stripped stem is not found in the dictionary, the service now attempts to append '다' (the standard citation form suffix) and checks again. This resolves the "Not found in dictionary" issue for verbs and adjectives (e.g., '먹었습니다' -> '먹다').

## TokenizerService Recursive Fix

### Summary
Updated `TokenizerService` to handle multiple suffixes recursively.

### Changes
-   **Recursive Stemming**: Updated `_process_token` to recursively strip endings. This solves issues where words have multiple suffixes (e.g., '먹었습니다' -> '먹었' -> '먹' -> '먹다').
-   **Predicate Handling**: Moved the '다' appending logic to the beginning of the function to support the recursive base case.

## TokenizerService Stemming Logic Update

### Summary
Updated `TokenizerService` to return the Stem instead of the Lemma (Dictionary Form), aligning with linguistic structure.

### Changes
-   **Stem Preference**: In `_process_token`, if a word matches a dictionary entry via `stem + "다"`, the service now returns the `stem` itself instead of the `lemma`.
-   **Validation Logic**: Updated the recursive validation logic to accept a stem if either the stem itself OR its lemma (`stem + "다"`) exists in the dictionary.

## Changelog Update

### Summary
Updated `changelog.md` to reflect the latest TokenizerService improvements.

### Changes
-   **Changelog**: Added entries for recursive suffix stripping and stem preference logic to the 1.0.0 release notes.