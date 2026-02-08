## 1.0.0 (2026-02-08)

Features:

- Enhanced Tokenizer
  - Add dictionary-based validation for smarter stemming
  - Support particle (josa) removal
  - Optimize performance with pre-computed suffix lists
  - Support recursive suffix stripping for complex conjugations
  - Improve predicate handling to return stems instead of dictionary forms

Refactor:

- Refactor TokenizerService for better code quality and PEP 8 compliance

Fix:

- Resolve numpy and pandas binary incompatibility

## 0.0.1 (2023-10-07)

Features:

- initial release
  - add NIADic reader and experimental tokenizer

Fix:

-