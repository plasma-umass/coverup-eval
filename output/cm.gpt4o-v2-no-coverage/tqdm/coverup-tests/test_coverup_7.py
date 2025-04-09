# file: tqdm/contrib/logging.py:18-34
# asked: {"lines": [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 33, 34], "branches": []}

import logging
import pytest
from tqdm.std import tqdm as std_tqdm
from unittest.mock import MagicMock, patch

from tqdm.contrib.logging import _TqdmLoggingHandler

@pytest.fixture
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    yield logger
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

def test_tqdm_logging_handler_emit(logger, monkeypatch):
    mock_tqdm_class = MagicMock()
    handler = _TqdmLoggingHandler(tqdm_class=mock_tqdm_class)
    logger.addHandler(handler)

    record = logging.LogRecord(name="test_logger", level=logging.INFO, pathname=__file__, lineno=10, msg="Test message", args=(), exc_info=None)
    
    with patch.object(handler, 'format', return_value="Formatted message") as mock_format:
        handler.emit(record)
        mock_format.assert_called_once_with(record)
        mock_tqdm_class.write.assert_called_once_with("Formatted message", file=handler.stream)
        handler.flush()

def test_tqdm_logging_handler_emit_with_exception(logger, monkeypatch):
    mock_tqdm_class = MagicMock()
    handler = _TqdmLoggingHandler(tqdm_class=mock_tqdm_class)
    logger.addHandler(handler)

    record = logging.LogRecord(name="test_logger", level=logging.INFO, pathname=__file__, lineno=10, msg="Test message", args=(), exc_info=None)
    
    with patch.object(handler, 'format', side_effect=ValueError("Formatting error")) as mock_format:
        with patch.object(handler, 'handleError') as mock_handle_error:
            handler.emit(record)
            mock_format.assert_called_once_with(record)
            mock_handle_error.assert_called_once_with(record)
