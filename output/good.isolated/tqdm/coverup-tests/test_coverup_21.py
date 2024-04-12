# file tqdm/contrib/logging.py:18-34
# lines [30, 32]
# branches []

import logging
from unittest.mock import Mock
import pytest
from tqdm.contrib.logging import _TqdmLoggingHandler

@pytest.fixture
def mock_tqdm_class(mocker):
    mock = mocker.Mock()
    mock.write = mocker.Mock()
    return mock

@pytest.fixture
def mock_stream(mocker):
    return mocker.Mock()

def test_tqdm_logging_handler_emit_with_flush_and_exception(mock_tqdm_class, mock_stream, mocker):
    handler = _TqdmLoggingHandler(tqdm_class=mock_tqdm_class)
    handler.stream = mock_stream

    record = logging.LogRecord(name="test", level=logging.INFO, pathname=__file__,
                               lineno=1, msg="test message", args=None, exc_info=None)

    # Simulate a flush that raises an exception
    mocker.patch.object(handler, 'flush', side_effect=RuntimeError("Flush failed"))
    mocker.patch.object(handler, 'handleError')

    # The RuntimeError is caught by the handler, so it does not propagate.
    # Therefore, we should not expect it to be raised.
    handler.emit(record)

    mock_tqdm_class.write.assert_called_once_with("test message", file=mock_stream)
    handler.flush.assert_called_once()
    handler.handleError.assert_called_once_with(record)
