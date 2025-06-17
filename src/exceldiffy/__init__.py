"""
exceldelta – A Python package for comparing Excel sheet columns and reporting differences.

Provides a simple interface to detect and display changes between two DataFrames,
centered around the Comparator class.
"""

__version__ = "0.1.1"
__author__ = "Israel Bosun"

from .comparator import Comparator

__all__ = [
    "Comparator",
    "__version__",
    "__author__",
]
