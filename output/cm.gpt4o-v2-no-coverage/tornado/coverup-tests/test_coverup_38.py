# file: tornado/log.py:211-258
# asked: {"lines": [211, 212, 219, 220, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 250, 251, 252, 254, 256, 257, 258], "branches": [[219, 220], [219, 223], [223, 224], [223, 225], [225, 226], [225, 227], [228, 229], [228, 254], [230, 231], [230, 237], [237, 238], [237, 246], [254, 0], [254, 256]]}
# gained: {"lines": [211, 212, 219, 220, 222, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 250, 251, 252, 254, 256, 257, 258], "branches": [[219, 220], [219, 223], [223, 224], [223, 225], [225, 227], [228, 229], [228, 254], [230, 231], [230, 237], [237, 238], [237, 246], [254, 0], [254, 256]]}

import pytest
import logging
from unittest.mock import MagicMock, patch
from tornado.log import enable_pretty_logging, LogFormatter

def test_enable_pretty_logging_no_options():
    with patch('tornado.options.options', create=True) as mock_options:
        mock_options.logging = None
        mock_options.log_file_prefix = None
        mock_options.log_to_stderr = None

        enable_pretty_logging()

        assert mock_options.logging is None

def test_enable_pretty_logging_logging_none():
    mock_options = MagicMock()
    mock_options.logging = "none"
    mock_options.log_file_prefix = None
    mock_options.log_to_stderr = None

    enable_pretty_logging(mock_options)

    assert mock_options.logging == "none"

def test_enable_pretty_logging_with_logger():
    mock_options = MagicMock()
    mock_options.logging = "info"
    mock_options.log_file_prefix = None
    mock_options.log_to_stderr = None

    mock_logger = MagicMock()

    enable_pretty_logging(mock_options, mock_logger)

    mock_logger.setLevel.assert_called_with(logging.INFO)

def test_enable_pretty_logging_log_file_prefix_size():
    mock_options = MagicMock()
    mock_options.logging = "info"
    mock_options.log_file_prefix = "test.log"
    mock_options.log_rotate_mode = "size"
    mock_options.log_file_max_size = 1000
    mock_options.log_file_num_backups = 1
    mock_options.log_to_stderr = None

    mock_logger = MagicMock()

    with patch('logging.handlers.RotatingFileHandler') as mock_handler:
        mock_handler_instance = mock_handler.return_value
        enable_pretty_logging(mock_options, mock_logger)

        mock_handler.assert_called_with(
            filename="test.log",
            maxBytes=1000,
            backupCount=1,
            encoding="utf-8"
        )
        mock_logger.addHandler.assert_called()
        assert isinstance(mock_handler_instance.setFormatter.call_args[0][0], LogFormatter)

def test_enable_pretty_logging_log_file_prefix_time():
    mock_options = MagicMock()
    mock_options.logging = "info"
    mock_options.log_file_prefix = "test.log"
    mock_options.log_rotate_mode = "time"
    mock_options.log_rotate_when = "midnight"
    mock_options.log_rotate_interval = 1
    mock_options.log_file_num_backups = 1
    mock_options.log_to_stderr = None

    mock_logger = MagicMock()

    with patch('logging.handlers.TimedRotatingFileHandler') as mock_handler:
        mock_handler_instance = mock_handler.return_value
        enable_pretty_logging(mock_options, mock_logger)

        mock_handler.assert_called_with(
            filename="test.log",
            when="midnight",
            interval=1,
            backupCount=1,
            encoding="utf-8"
        )
        mock_logger.addHandler.assert_called()
        assert isinstance(mock_handler_instance.setFormatter.call_args[0][0], LogFormatter)

def test_enable_pretty_logging_log_file_prefix_invalid():
    mock_options = MagicMock()
    mock_options.logging = "info"
    mock_options.log_file_prefix = "test.log"
    mock_options.log_rotate_mode = "invalid"
    mock_options.log_to_stderr = None

    mock_logger = MagicMock()

    with pytest.raises(ValueError, match='The value of log_rotate_mode option should be "size" or "time", not "invalid".'):
        enable_pretty_logging(mock_options, mock_logger)

def test_enable_pretty_logging_log_to_stderr():
    mock_options = MagicMock()
    mock_options.logging = "info"
    mock_options.log_file_prefix = None
    mock_options.log_to_stderr = True

    mock_logger = MagicMock()

    with patch('logging.StreamHandler') as mock_handler:
        mock_handler_instance = mock_handler.return_value
        enable_pretty_logging(mock_options, mock_logger)

        mock_handler.assert_called()
        mock_logger.addHandler.assert_called()
        assert isinstance(mock_handler_instance.setFormatter.call_args[0][0], LogFormatter)
