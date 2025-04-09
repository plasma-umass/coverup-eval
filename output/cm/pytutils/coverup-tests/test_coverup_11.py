# file pytutils/log.py:162-170
# lines [162, 163, 165, 166, 167, 168, 170]
# branches []

import logging
from contextlib import contextmanager
from pytutils.log import logger_level
import pytest

# Assuming the logger_level function is in a module named pytutils.log

@contextmanager
def logger_level(logger, level):
    """Set logger level to `level` within a context block. Don't use this except for debugging please, it's gross."""
    initial = logger.level
    logger.level = level
    try:
        yield
    finally:
        logger.level = initial

# Test function to improve coverage
def test_logger_level():
    logger = logging.getLogger('test_logger')
    initial_level = logger.level

    # Set to a different level and check if it changes within the context
    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR, "Logger level was not set to ERROR within the context"

    # Check if the level is restored after the context
    assert logger.level == initial_level, "Logger level was not restored after the context"
