"""
Base classes and data structures for the application.

This module provides fundamental building blocks for immutable data structures
used throughout the application, ensuring consistency and type safety.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class BaseFrozen:
    """Base class for immutable data structures."""
    pass