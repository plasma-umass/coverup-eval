# file tornado/log.py:211-258
# lines [211, 212, 219, 220, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 250, 251, 252, 254, 256, 257, 258]
# branches ['219->220', '219->223', '223->224', '223->225', '225->226', '225->227', '228->229', '228->254', '230->231', '230->237', '237->238', '237->246', '254->exit', '254->256']

import logging
import pytest
from unittest import mock
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
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert logger.level == logging.INFO

def test_enable_pretty_logging_none_logging(mock_options):
    mock_options.logging = None
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert logger.level != logging.INFO

def test_enable_pretty_logging_log_file_prefix_size(mock_options):
    mock_options.log_file_prefix = "test_log"
    mock_options.log_rotate_mode = "size"
    mock_options.log_file_max_size = 1000
    mock_options.log_file_num_backups = 1
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.handlers.RotatingFileHandler) for handler in logger.handlers)

def test_enable_pretty_logging_log_file_prefix_time(mock_options):
    mock_options.log_file_prefix = "test_log"
    mock_options.log_rotate_mode = "time"
    mock_options.log_rotate_when = "midnight"
    mock_options.log_rotate_interval = 1
    mock_options.log_file_num_backups = 1
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.handlers.TimedRotatingFileHandler) for handler in logger.handlers)

def test_enable_pretty_logging_invalid_rotate_mode(mock_options):
    mock_options.log_file_prefix = "test_log"
    mock_options.log_rotate_mode = "invalid_mode"
    with mock.patch('tornado.options.options', mock_options):
        with pytest.raises(ValueError, match='The value of log_rotate_mode option should be "size" or "time"'):
            enable_pretty_logging()

def test_enable_pretty_logging_log_to_stderr(mock_options):
    mock_options.log_to_stderr = True
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)

def test_enable_pretty_logging_log_to_stderr_none(mock_options):
    mock_options.log_to_stderr = None
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)

@pytest.fixture(autouse=True)
def cleanup_logging():
    yield
    logger = logging.getLogger()
    logger.handlers = []
    logger.setLevel(logging.NOTSET)
