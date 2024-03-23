# file tornado/log.py:211-258
# lines [226]
# branches ['225->226']

import logging
import pytest
from tornado.log import enable_pretty_logging
from unittest.mock import Mock

@pytest.fixture
def mock_logging(mocker):
    logger = logging.getLogger("tornado.test")
    mocker.patch.object(logging, 'getLogger', return_value=logger)
    return logger

@pytest.fixture
def mock_options(mocker):
    options = Mock()
    options.logging = "info"
    options.log_file_prefix = None
    options.log_to_stderr = None
    return options

def test_enable_pretty_logging_with_no_logger_provided(mock_logging, mock_options):
    # Ensure that the logger has no handlers before the test
    mock_logging.handlers = []
    assert not mock_logging.handlers

    # Call the function with no logger provided
    enable_pretty_logging(options=mock_options)

    # Check that the logger now has a handler (StreamHandler) added
    assert len(mock_logging.handlers) == 1
    assert isinstance(mock_logging.handlers[0], logging.StreamHandler)

    # Clean up by removing the added handler
    mock_logging.handlers = []
