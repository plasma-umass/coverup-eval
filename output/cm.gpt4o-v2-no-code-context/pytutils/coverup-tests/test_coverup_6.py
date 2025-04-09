# file: pytutils/log.py:162-170
# asked: {"lines": [162, 163, 165, 166, 167, 168, 170], "branches": []}
# gained: {"lines": [162, 163], "branches": []}

import logging
import pytest
from contextlib import contextmanager
from pytutils.log import logger_level

@contextmanager
def logger_level(logger, level):
    """Set logger level to `level` within a context block. Don't use this except for debugging please, it's gross."""
    initial = logger.level
    logger.level = level
    try:
        yield
    finally:
        logger.level = initial

def test_logger_level(monkeypatch):
    logger = logging.getLogger('test_logger')
    initial_level = logger.level
    new_level = logging.DEBUG

    with logger_level(logger, new_level):
        assert logger.level == new_level

    assert logger.level == initial_level

    # Clean up
    monkeypatch.undo()
