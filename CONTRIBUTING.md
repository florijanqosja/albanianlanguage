# Contributing to Albanian Language Package

Thank you for your interest in contributing to the Albanian Language package! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct: be respectful, considerate, and collaborative.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with the following information:
- Clear title and description
- Steps to reproduce the issue
- Expected and actual behavior
- Screenshots or code samples if applicable
- Your environment information

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- Clear title and description
- Step-by-step explanation of the enhancement
- Expected benefits
- Any examples or references

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure they pass
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone your fork of the repository
2. Install development dependencies:
   ```
   pip install -e .
   pip install -r requirements-dev.txt
   ```
3. Make sure tests pass:
   ```
   pytest
   ```
4. Follow code style guidelines (we use black, isort, and flake8)

## Code Style

- Follow PEP 8 guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Sort imports with [isort](https://pycqa.github.io/isort/)
- Add type hints where appropriate

## Testing

All new code should have tests. Run tests with:

```
pytest
```

For coverage report:

```
pytest --cov=albanianlanguage
```

## Documentation

Please document all functions, classes, and code using docstrings in the Google style.

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

## Questions?

If you have any questions, please open an issue for discussion. 