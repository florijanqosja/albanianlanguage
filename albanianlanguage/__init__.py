"""
Albanian Language Package

A comprehensive package for Albanian language processing,
providing access to a dataset of words with filtering capabilities.
"""

from .words import get_all_words
from .__version__ import __version__

__all__ = ["get_all_words", "__version__"]