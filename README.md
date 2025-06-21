# 🇦🇱 Albanian Language Package

[![PyPI version](https://img.shields.io/pypi/v/albanianlanguage.svg)](https://pypi.org/project/albanianlanguage/)
[![Tests](https://github.com/florijanqosja/albanianlanguage/actions/workflows/test.yml/badge.svg)](https://github.com/florijanqosja/albanianlanguage/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/albanianlanguage.svg)](https://pypi.org/project/albanianlanguage/)

A comprehensive Python package for processing and working with the Albanian language. This package provides access to Albanian words with filtering capabilities and detailed linguistic information.

## 🚀 Features

- **Word Access**: Retrieve Albanian words with powerful filtering options
- **Linguistic Details**: Get word types and definitions
- **Efficient Processing**: Optimized for performance with large datasets
- **Simple API**: Easy to integrate into any NLP or language processing pipeline

## 📦 Installation

Install the package directly from PyPI:

```bash
pip install albanianlanguage
```

## 🔍 Usage

### Basic Usage

```python
from albanianlanguage import get_all_words

# Get all Albanian words
all_words = get_all_words()
print(f"Total words: {len(all_words)}")

# Get words starting with a specific prefix
sh_words = get_all_words(starts_with="sh")
print(f"Words starting with 'sh': {len(sh_words)}")
```

### Filtering Words

```python
# Get words containing a specific substring
words_with_je = get_all_words(includes="je")
print(f"Words containing 'je': {len(words_with_je)}")
```

### Getting Word Details

```python
# Get words with their types and definitions
detailed_words = get_all_words(return_type=True, return_definition=True)

# Print some examples
for word in detailed_words[:5]:
    print(f"Word: {word['word']}")
    print(f"Type: {word.get('type', 'N/A')}")
    print(f"Definition: {word.get('definition', 'N/A')}")
    print("---")
```

## 📚 API Reference

### `get_all_words(starts_with=None, includes=None, return_type=False, return_definition=False)`

Retrieves Albanian words based on filtering criteria.

**Parameters:**
- `starts_with` (str, optional): If provided, only returns words that start with this substring
- `includes` (str, optional): If provided, only returns words that contain this substring
- `return_type` (bool, optional): If True, includes word types in the result
- `return_definition` (bool, optional): If True, includes word definitions in the result

**Returns:**
- When `return_type=False` and `return_definition=False`: List of strings (words)
- Otherwise: List of dictionaries with word details

## 🤝 Contributing

Contributions are welcome! Check out the [Contributing Guidelines](CONTRIBUTING.md) to get started.

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/florijanqosja/albanianlanguage.git
   cd albanianlanguage
   ```

2. Install development dependencies:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

## ❓ Support

If you encounter any issues or have questions, please [file an issue](https://github.com/florijanqosja/albanianlanguage/issues).

## 🚀 Support the Project

If you find this project helpful, please consider supporting its development:

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub-ea4aaa)](https://github.com/sponsors/florijanqosja)
[![Ko-fi](https://img.shields.io/badge/Support-Ko--fi-FF5E5B)](https://ko-fi.com/albanian_language)
[![Buy Me A Coffee](https://img.shields.io/badge/Support-Buy%20Me%20A%20Coffee-yellow)](https://www.buymeacoffee.com/albanianlanguage)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
