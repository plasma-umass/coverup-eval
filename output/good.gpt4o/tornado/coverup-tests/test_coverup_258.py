# file tornado/log.py:211-258
# lines []
# branches ['225->227']

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

def test_enable_pretty_logging_no_logger(mock_options, mocker):
    mocker.patch('tornado.options.options', mock_options)
    mock_logger = mocker.patch('logging.getLogger', return_value=logging.getLogger('test_logger'))
    
    enable_pretty_logging(options=mock_options, logger=None)
    
    mock_logger.assert_called_once()
    assert mock_logger.return_value.level == logging.INFO

def test_enable_pretty_logging_with_logger(mock_options):
    test_logger = logging.getLogger('test_logger')
    enable_pretty_logging(options=mock_options, logger=test_logger)
    
    assert test_logger.level == logging.INFO

@pytest.fixture(autouse=True)
def cleanup_logging():
    yield
    logging.getLogger('test_logger').handlers.clear()
