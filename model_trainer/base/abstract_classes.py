"""
abstract_classes.py
Description: Module defining abstract base classes for composable components
"""

# Define imports
from abc import ABC, abstractmethod

from torch.nn import Module

from model_trainer.src.config import CONTEXT
from model_trainer.lib.logger import create_logger


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

    logger = create_logger(CONTEXT["log_level"])
    try:
        model = ModelABC()
    except TypeError as exc_type:
        logger.error(
            "Caught expected TypeError. Printing contents of TypeError exception..."
        )
        logger.error(exc_type)
