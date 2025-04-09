# file: pytutils/log.py:162-170
# asked: {"lines": [162, 163, 165, 166, 167, 168, 170], "branches": []}
# gained: {"lines": [162, 163, 165, 166, 167, 168, 170], "branches": []}

import logging
import pytest
from contextlib import contextmanager
from pytutils.log import logger_level

def test_logger_level(monkeypatch):
    logger = logging.getLogger('test_logger')
    initial_level = logger.level

    with logger_level(logger, logging.DEBUG):
        assert logger.level == logging.DEBUG

    assert logger.level == initial_level

    with logger_level(logger, logging.ERROR):
        assert logger.level == logging.ERROR

    assert logger.level == initial_level

    # Test exception handling within the context manager
    try:
        with logger_level(logger, logging.WARNING):
            assert logger.level == logging.WARNING
            raise ValueError("Test exception")
    except ValueError:
        pass

    assert logger.level == initial_level
