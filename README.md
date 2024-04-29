# AlbanianLanguage Package

The `AlbanianLanguage` package is a comprehensive toolkit designed for handling various linguistic tasks associated with the Albanian language. It offers functionalities to read words from a CSV file, apply filters based on specific criteria, and optionally include additional details such as word types and definitions.

## Installation

Install `AlbanianLanguage` directly from PyPI:

```bash
pip install albanianlanguage
```

## Usage

To use the AlbanianLanguage package, import and call its main functions:

```
from albanianlanguage import get_all_words

# Get all words from the specified CSV
words = get_all_words()

# Get words that start with "ka"
ex_words = get_all_words(starts_with="ka")

# Get words that include "pse"
ample_words = get_all_words(includes="pse")

# Get words along with their types and definitions
detailed_words = get_all_words(return_type=True, return_definition=True)
```

## Parameters

- filename (str): Path to the CSV file. Defaults to 'albanianlanguage/ff.csv'.
- starts_with (str, optional): Filter words that start with this substring.
- includes (str, optional): Filter words that include this substring.
- return_type (bool, optional): If true, includes the word's type in the output.
- return_definition (bool, optional): If true, includes the word's definition in the output.

## Features

Efficiently read and filter words from a CSV file.
Optionally retrieve additional linguistic details such as type and definition.
Designed specifically for applications related to the Albanian language.
Requirements
This package requires Python 3.x. No additional libraries are needed for the basic functionality, but make sure to handle dependencies if you expand the package.

## **Pushing to PYPI**

```python
!pip install setuptools wheel twine # Install the necessary tools:

!python setup.py sdist bdist_wheel # Generate distribution archives:

!rm -rf dist # if there are any previous builds

!twine upload dist/* # Upload the distribution to PyPI:
```

## Contributing

Contributions to AlbanianLanguage are warmly welcomed. Please fork the repository, make your changes, and submit a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
