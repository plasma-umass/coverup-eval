# file cookiecutter/log.py:19-51
# lines [19, 26, 27, 31, 34, 35, 36, 37, 38, 39, 42, 43, 46, 47, 48, 49, 51]
# branches ['34->35', '34->42']

import logging
import pytest
from cookiecutter.log import configure_logger

LOG_FORMATS = {
    'DEBUG': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'INFO': '%(name)s - %(levelname)s - %(message)s',
    'WARNING': '%(levelname)s - %(message)s',
}

LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
}

@pytest.fixture
def debug_log_file(tmp_path):
    return tmp_path / "debug.log"

def test_configure_logger_with_file_handler(debug_log_file, mocker):
    # Mock the FileHandler to prevent actual file creation
    file_handler_mock = mocker.patch('logging.FileHandler', autospec=True)
    
    # Configure the logger with a debug file
    logger = configure_logger(stream_level='INFO', debug_file=str(debug_log_file))
    
    # Check that the logger has two handlers (file and stream)
    assert len(logger.handlers) == 2
    
    # Check that the first handler is a FileHandler by checking the mock
    assert file_handler_mock.called
    
    # Check that the second handler is a StreamHandler
    assert isinstance(logger.handlers[1], logging.StreamHandler)
    
    # Check that the stream handler is set to the INFO level
    assert logger.handlers[1].level == logging.INFO
    
    # Check that the file handler mock is set to the DEBUG level
    file_handler_instance = file_handler_mock.return_value
    file_handler_instance.setLevel.assert_called_once_with(logging.DEBUG)
    
    # Clean up by removing handlers
    logger.handlers.clear()
