# file: tornado/log.py:211-258
# asked: {"lines": [226], "branches": [[225, 226]]}
# gained: {"lines": [226], "branches": [[225, 226]]}

import logging
import pytest
from unittest import mock
from tornado.log import enable_pretty_logging

class MockOptions:
    def __init__(self, logging=None, log_file_prefix=None, log_rotate_mode=None, log_file_max_size=None, log_file_num_backups=None, log_rotate_when=None, log_rotate_interval=None, log_to_stderr=None):
        self.logging = logging
        self.log_file_prefix = log_file_prefix
        self.log_rotate_mode = log_rotate_mode
        self.log_file_max_size = log_file_max_size
        self.log_file_num_backups = log_file_num_backups
        self.log_rotate_when = log_rotate_when
        self.log_rotate_interval = log_rotate_interval
        self.log_to_stderr = log_to_stderr

def test_enable_pretty_logging_default_logger(monkeypatch):
    options = MockOptions(logging="info")
    with mock.patch('logging.getLogger') as mock_get_logger:
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        enable_pretty_logging(options=options)

        mock_get_logger.assert_called_once()
        mock_logger.setLevel.assert_called_once_with(logging.INFO)

@pytest.mark.parametrize("log_rotate_mode", ["size", "time"])
def test_enable_pretty_logging_file_handler(monkeypatch, log_rotate_mode):
    options = MockOptions(
        logging="info",
        log_file_prefix="test.log",
        log_rotate_mode=log_rotate_mode,
        log_file_max_size=1000,
        log_file_num_backups=1,
        log_rotate_when="midnight",
        log_rotate_interval=1
    )
    with mock.patch('logging.getLogger') as mock_get_logger, \
         mock.patch('logging.handlers.RotatingFileHandler') as mock_rotating_handler, \
         mock.patch('logging.handlers.TimedRotatingFileHandler') as mock_timed_handler:
        
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        enable_pretty_logging(options=options)

        mock_get_logger.assert_called_once()
        mock_logger.setLevel.assert_called_once_with(logging.INFO)
        if log_rotate_mode == "size":
            mock_rotating_handler.assert_called_once()
        elif log_rotate_mode == "time":
            mock_timed_handler.assert_called_once()

def test_enable_pretty_logging_invalid_rotate_mode(monkeypatch):
    options = MockOptions(
        logging="info",
        log_file_prefix="test.log",
        log_rotate_mode="invalid_mode"
    )
    with mock.patch('logging.getLogger') as mock_get_logger:
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        with pytest.raises(ValueError, match='The value of log_rotate_mode option should be "size" or "time", not "invalid_mode".'):
            enable_pretty_logging(options=options)

def test_enable_pretty_logging_log_to_stderr(monkeypatch):
    options = MockOptions(logging="info", log_to_stderr=True)
    with mock.patch('logging.getLogger') as mock_get_logger, \
         mock.patch('logging.StreamHandler') as mock_stream_handler:
        
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        enable_pretty_logging(options=options)

        mock_get_logger.assert_called_once()
        mock_logger.setLevel.assert_called_once_with(logging.INFO)
        mock_stream_handler.assert_called_once()
