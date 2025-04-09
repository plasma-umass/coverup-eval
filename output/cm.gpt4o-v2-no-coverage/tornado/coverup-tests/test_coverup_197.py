# file: tornado/log.py:211-258
# asked: {"lines": [226], "branches": [[225, 226]]}
# gained: {"lines": [226], "branches": [[225, 226]]}

import pytest
import logging
from unittest.mock import patch, MagicMock
from tornado.log import enable_pretty_logging, LogFormatter

@pytest.fixture
def mock_options():
    class MockOptions:
        logging = "info"
        log_file_prefix = None
        log_rotate_mode = None
        log_file_max_size = None
        log_file_num_backups = None
        log_rotate_when = None
        log_rotate_interval = None
        log_to_stderr = None

    return MockOptions()

def test_enable_pretty_logging_no_options(mock_options):
    with patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert logger.level == logging.INFO

def test_enable_pretty_logging_none_logging(mock_options):
    mock_options.logging = None
    with patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert logger.level != logging.INFO

def test_enable_pretty_logging_log_file_prefix_size(mock_options):
    mock_options.log_file_prefix = "test.log"
    mock_options.log_rotate_mode = "size"
    mock_options.log_file_max_size = 1000
    mock_options.log_file_num_backups = 1

    with patch('tornado.options.options', mock_options):
        with patch('logging.handlers.RotatingFileHandler') as mock_handler:
            enable_pretty_logging()
            mock_handler.assert_called_once_with(
                filename="test.log",
                maxBytes=1000,
                backupCount=1,
                encoding="utf-8"
            )

def test_enable_pretty_logging_log_file_prefix_time(mock_options):
    mock_options.log_file_prefix = "test.log"
    mock_options.log_rotate_mode = "time"
    mock_options.log_rotate_when = "midnight"
    mock_options.log_rotate_interval = 1
    mock_options.log_file_num_backups = 1

    with patch('tornado.options.options', mock_options):
        with patch('logging.handlers.TimedRotatingFileHandler') as mock_handler:
            enable_pretty_logging()
            mock_handler.assert_called_once_with(
                filename="test.log",
                when="midnight",
                interval=1,
                backupCount=1,
                encoding="utf-8"
            )

def test_enable_pretty_logging_invalid_rotate_mode(mock_options):
    mock_options.log_file_prefix = "test.log"
    mock_options.log_rotate_mode = "invalid_mode"

    with patch('tornado.options.options', mock_options):
        with pytest.raises(ValueError, match='The value of log_rotate_mode option should be "size" or "time", not "invalid_mode".'):
            enable_pretty_logging()

def test_enable_pretty_logging_log_to_stderr(mock_options):
    mock_options.log_to_stderr = True

    with patch('tornado.options.options', mock_options):
        with patch('logging.StreamHandler') as mock_handler:
            enable_pretty_logging()
            mock_handler.assert_called_once()

def test_enable_pretty_logging_no_handlers(mock_options):
    mock_options.log_to_stderr = None

    with patch('tornado.options.options', mock_options):
        logger = logging.getLogger()
        logger.handlers = []
        with patch('logging.StreamHandler') as mock_handler:
            enable_pretty_logging()
            mock_handler.assert_called_once()
