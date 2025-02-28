"""
logger.py
Description: Module that sets up a logger for consistent logs
"""

import logging

from model_trainer.src.config import CONTEXT


def create_logger(level):

    # Create logger, formatter, and handlers for different message types
    i_logger = logging.getLogger(__name__)
    i_logger.setLevel(level)

    default_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(default_formatter)
    i_logger.addHandler(handler)

    return i_logger


# Self-test
if __name__ == "__main__":

    logger = create_logger(CONTEXT["log_level"])
    logger.error("error message")
    logger.warning("warning message")
    logger.info("info message")
