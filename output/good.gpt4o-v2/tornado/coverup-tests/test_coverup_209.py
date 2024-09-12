# file: tornado/log.py:211-258
# asked: {"lines": [219, 220, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 250, 251, 252, 254, 256, 257, 258], "branches": [[219, 220], [219, 223], [223, 224], [223, 225], [225, 226], [225, 227], [228, 229], [228, 254], [230, 231], [230, 237], [237, 238], [237, 246], [254, 0], [254, 256]]}
# gained: {"lines": [219, 220, 222, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 250, 251, 252, 254, 256, 257, 258], "branches": [[219, 220], [219, 223], [223, 224], [223, 225], [225, 227], [228, 229], [228, 254], [230, 231], [230, 237], [237, 238], [237, 246], [254, 0], [254, 256]]}

import pytest
import logging
from unittest.mock import Mock, patch

from tornado.log import enable_pretty_logging, LogFormatter

class MockOptions:
    def __init__(self, logging=None, log_file_prefix=None, log_rotate_mode=None, log_file_max_size=0,
                 log_file_num_backups=0, log_rotate_when=None, log_rotate_interval=0, log_to_stderr=None):
        self.logging = logging
        self.log_file_prefix = log_file_prefix
        self.log_rotate_mode = log_rotate_mode
        self.log_file_max_size = log_file_max_size
        self.log_file_num_backups = log_file_num_backups
        self.log_rotate_when = log_rotate_when
        self.log_rotate_interval = log_rotate_interval
        self.log_to_stderr = log_to_stderr

@pytest.fixture
def mock_logger():
    logger = logging.getLogger("tornado_test_logger")
    logger.setLevel(logging.NOTSET)
    logger.handlers = []
    yield logger
    logger.handlers = []

def test_enable_pretty_logging_no_options(mock_logger):
    with patch("tornado.options.options", MockOptions(logging="warning")):
        enable_pretty_logging(logger=mock_logger)
        assert mock_logger.level == logging.WARNING

def test_enable_pretty_logging_no_logging(mock_logger):
    options = MockOptions(logging=None)
    enable_pretty_logging(options=options, logger=mock_logger)
    assert mock_logger.level == logging.NOTSET

def test_enable_pretty_logging_log_file_prefix_size(mock_logger):
    options = MockOptions(logging="info", log_file_prefix="test.log", log_rotate_mode="size", log_file_max_size=1000,
                          log_file_num_backups=1)
    with patch("logging.handlers.RotatingFileHandler") as mock_handler:
        mock_handler_instance = mock_handler.return_value
        enable_pretty_logging(options=options, logger=mock_logger)
        mock_handler.assert_called_once_with(filename="test.log", maxBytes=1000, backupCount=1, encoding="utf-8")
        assert isinstance(mock_handler_instance.setFormatter.call_args[0][0], LogFormatter)

def test_enable_pretty_logging_log_file_prefix_time(mock_logger):
    options = MockOptions(logging="info", log_file_prefix="test.log", log_rotate_mode="time", log_rotate_when="midnight",
                          log_rotate_interval=1, log_file_num_backups=1)
    with patch("logging.handlers.TimedRotatingFileHandler") as mock_handler:
        mock_handler_instance = mock_handler.return_value
        enable_pretty_logging(options=options, logger=mock_logger)
        mock_handler.assert_called_once_with(filename="test.log", when="midnight", interval=1, backupCount=1, encoding="utf-8")
        assert isinstance(mock_handler_instance.setFormatter.call_args[0][0], LogFormatter)

def test_enable_pretty_logging_invalid_rotate_mode(mock_logger):
    options = MockOptions(logging="info", log_file_prefix="test.log", log_rotate_mode="invalid")
    with pytest.raises(ValueError, match='The value of log_rotate_mode option should be "size" or "time", not "invalid".'):
        enable_pretty_logging(options=options, logger=mock_logger)

def test_enable_pretty_logging_log_to_stderr(mock_logger):
    options = MockOptions(logging="info", log_to_stderr=True)
    with patch("logging.StreamHandler") as mock_handler:
        mock_handler_instance = mock_handler.return_value
        enable_pretty_logging(options=options, logger=mock_logger)
        mock_handler.assert_called_once()
        assert isinstance(mock_handler_instance.setFormatter.call_args[0][0], LogFormatter)

def test_enable_pretty_logging_log_to_stderr_default(mock_logger):
    options = MockOptions(logging="info", log_to_stderr=None)
    with patch("logging.StreamHandler") as mock_handler:
        mock_handler_instance = mock_handler.return_value
        enable_pretty_logging(options=options, logger=mock_logger)
        mock_handler.assert_called_once()
        assert isinstance(mock_handler_instance.setFormatter.call_args[0][0], LogFormatter)
