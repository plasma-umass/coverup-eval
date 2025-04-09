# file tornado/log.py:211-258
# lines [211, 212, 219, 220, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 250, 251, 252, 254, 256, 257, 258]
# branches ['219->220', '219->223', '223->224', '223->225', '225->226', '225->227', '228->229', '228->254', '230->231', '230->237', '237->238', '237->246', '254->exit', '254->256']

import logging
import pytest
from unittest.mock import Mock
from tornado.log import enable_pretty_logging, LogFormatter


@pytest.fixture
def mock_options():
    mock = Mock()
    mock.logging = 'info'
    mock.log_file_prefix = None
    mock.log_to_stderr = True
    return mock


@pytest.fixture
def mock_logger():
    return Mock(spec=logging.Logger)


def test_enable_pretty_logging_with_none_options(mock_logger, mocker):
    mocker.patch('tornado.options.options', logging='info', log_file_prefix=None, log_to_stderr=True)
    enable_pretty_logging(None, mock_logger)
    mock_logger.setLevel.assert_called_with(logging.INFO)
    mock_logger.addHandler.assert_called_once()
    handler = mock_logger.addHandler.call_args[0][0]
    assert isinstance(handler, logging.StreamHandler), "Handler should be a StreamHandler"
    assert isinstance(handler.formatter, LogFormatter), "Formatter should be a LogFormatter"


def test_enable_pretty_logging_with_none_logging(mock_options, mock_logger):
    mock_options.logging = None
    enable_pretty_logging(mock_options, mock_logger)
    mock_logger.setLevel.assert_not_called()
    mock_logger.addHandler.assert_not_called()


def test_enable_pretty_logging_with_log_to_stderr_false(mock_options, mock_logger):
    mock_options.log_to_stderr = False
    enable_pretty_logging(mock_options, mock_logger)
    mock_logger.setLevel.assert_called_with(logging.INFO)
    mock_logger.addHandler.assert_not_called()


def test_enable_pretty_logging_with_log_file_prefix(mock_options, mock_logger, mocker):
    mock_options.log_file_prefix = 'test.log'
    mock_options.log_rotate_mode = 'size'
    mock_options.log_file_max_size = 1000000
    mock_options.log_file_num_backups = 3
    mocker.patch('logging.handlers.RotatingFileHandler')
    enable_pretty_logging(mock_options, mock_logger)
    mock_logger.setLevel.assert_called_with(logging.INFO)
    logging.handlers.RotatingFileHandler.assert_called_once_with(
        filename='test.log',
        maxBytes=1000000,
        backupCount=3,
        encoding='utf-8'
    )


def test_enable_pretty_logging_with_invalid_rotate_mode(mock_options, mock_logger):
    mock_options.log_file_prefix = 'test.log'
    mock_options.log_rotate_mode = 'invalid'
    with pytest.raises(ValueError) as exc_info:
        enable_pretty_logging(mock_options, mock_logger)
    assert "The value of log_rotate_mode option should be \"size\" or \"time\", not \"invalid\"." in str(exc_info.value)


def test_enable_pretty_logging_with_time_rotate_mode(mock_options, mock_logger, mocker):
    mock_options.log_file_prefix = 'test.log'
    mock_options.log_rotate_mode = 'time'
    mock_options.log_rotate_when = 'midnight'
    mock_options.log_rotate_interval = 1
    mock_options.log_file_num_backups = 3
    mocker.patch('logging.handlers.TimedRotatingFileHandler')
    enable_pretty_logging(mock_options, mock_logger)
    mock_logger.setLevel.assert_called_with(logging.INFO)
    logging.handlers.TimedRotatingFileHandler.assert_called_once_with(
        filename='test.log',
        when='midnight',
        interval=1,
        backupCount=3,
        encoding='utf-8'
    )
