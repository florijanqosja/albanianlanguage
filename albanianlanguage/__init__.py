"""
Albanian Language Package

A comprehensive package for Albanian language processing,
providing access to a dataset of words with filtering capabilities.
"""

from .__version__ import __version__
from .words import get_all_words

__all__ = ["get_all_words", "__version__"]
