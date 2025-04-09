# file pytutils/log.py:162-170
# lines [165, 166, 167, 168, 170]
# branches []

import logging
from contextlib import contextmanager
from pytutils.log import logger_level
import pytest

# Assuming the logger_level function is part of a module named pytutils.log
# and the file structure is as follows:
# pytutils/
# ├── __init__.py
# └── log.py

# The test function to cover lines 165-170
def test_logger_level(mocker):
    # Create a mock logger
    mock_logger = mocker.MagicMock(spec=logging.Logger)
    mock_logger.level = 10  # Set an initial level

    # Use the logger_level context manager
    with logger_level(mock_logger, 20):
        # Inside the context, the logger's level should be set to 20
        assert mock_logger.level == 20

    # After the context, the logger's level should be reset to the initial level
    assert mock_logger.level == 10
