# file tornado/log.py:211-258
# lines [226]
# branches ['225->226']

import logging
import pytest
from tornado.log import enable_pretty_logging
from tornado.options import options, parse_command_line
from unittest.mock import patch, MagicMock

@pytest.fixture
def logger():
    return logging.getLogger('tornado.test')

@pytest.fixture
def reset_options():
    # Backup original options
    backup = {name: getattr(options, name) for name in options}
    yield
    # Restore original options after test
    for name, value in backup.items():
        setattr(options, name, value)

@pytest.fixture
def mock_logging_handler():
    with patch('logging.getLogger') as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        yield mock_logger

def test_enable_pretty_logging_with_none_logger(mock_logging_handler, reset_options):
    # Set the options to trigger the creation of a logger
    options.logging = "info"
    options.log_to_stderr = True
    options.log_file_prefix = None  # Ensure no file logging is configured

    # Call the function with logger set to None
    enable_pretty_logging(options=options, logger=None)

    # Check that a logger was created and handlers were added
    mock_logging_handler.setLevel.assert_called_with(logging.INFO)
    assert mock_logging_handler.addHandler.called

    # Check that no file handlers were added since log_file_prefix is None
    assert not any(isinstance(handler, logging.FileHandler) for handler in mock_logging_handler.handlers)

    # Clean up by removing any handlers that were added
    for handler in mock_logging_handler.handlers:
        mock_logging_handler.removeHandler(handler)
