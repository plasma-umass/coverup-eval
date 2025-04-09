# file: pytutils/log.py:162-170
# asked: {"lines": [162, 163, 165, 166, 167, 168, 170], "branches": []}
# gained: {"lines": [162, 163, 165, 166, 167, 168, 170], "branches": []}

import logging
import pytest
from contextlib import contextmanager
from pytutils.log import logger_level

def test_logger_level():
    logger = logging.getLogger('test_logger')
    initial_level = logger.level
    new_level = logging.DEBUG

    with logger_level(logger, new_level):
        assert logger.level == new_level

    assert logger.level == initial_level
