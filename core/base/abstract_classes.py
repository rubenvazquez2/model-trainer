"""
abstract_classes.py
Description: Module defining abstract base classes for composable components
"""

# Define imports
from abc import ABC, abstractmethod

from torch.nn import Module


class ModelABC(ABC, Module):
    """
    ModelABC
    Description: Abstract base class describing Model objects
    """

    @abstractmethod
    def forward(self, X, y):
        pass


# Self-test
if __name__ == "__main__":

    try:
        model = ModelABC()
    except TypeError as exc_type:
        print("Caught expected TypeError. Printing contents of TypeError exception...")
        print(exc_type)
