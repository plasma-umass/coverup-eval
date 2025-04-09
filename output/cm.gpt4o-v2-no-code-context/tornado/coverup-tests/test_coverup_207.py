# file: tornado/log.py:211-258
# asked: {"lines": [], "branches": [[225, 227]]}
# gained: {"lines": [], "branches": [[225, 227]]}

import logging
import pytest
from tornado.log import enable_pretty_logging
from unittest import mock

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

def test_enable_pretty_logging_with_default_logger(mock_options):
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert logger.level == logging.INFO

def test_enable_pretty_logging_with_custom_logger(mock_options):
    custom_logger = logging.getLogger('custom')
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging(logger=custom_logger)
        assert custom_logger.level == logging.INFO

def test_enable_pretty_logging_with_none_logging(mock_options):
    mock_options.logging = None
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert logger.level != logging.INFO  # Should not change the level

def test_enable_pretty_logging_with_invalid_rotate_mode(mock_options):
    mock_options.log_file_prefix = 'test.log'
    mock_options.log_rotate_mode = 'invalid_mode'
    with mock.patch('tornado.options.options', mock_options):
        with pytest.raises(ValueError, match='The value of log_rotate_mode option should be "size" or "time"'):
            enable_pretty_logging()

def test_enable_pretty_logging_with_size_rotate_mode(mock_options):
    mock_options.log_file_prefix = 'test.log'
    mock_options.log_rotate_mode = 'size'
    mock_options.log_file_max_size = 1000
    mock_options.log_file_num_backups = 1
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.handlers.RotatingFileHandler) for handler in logger.handlers)

def test_enable_pretty_logging_with_time_rotate_mode(mock_options):
    mock_options.log_file_prefix = 'test.log'
    mock_options.log_rotate_mode = 'time'
    mock_options.log_rotate_when = 'midnight'
    mock_options.log_rotate_interval = 1
    mock_options.log_file_num_backups = 1
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.handlers.TimedRotatingFileHandler) for handler in logger.handlers)

def test_enable_pretty_logging_with_log_to_stderr(mock_options):
    mock_options.log_to_stderr = True
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)

def test_enable_pretty_logging_with_no_handlers(mock_options):
    mock_options.log_to_stderr = None
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)
