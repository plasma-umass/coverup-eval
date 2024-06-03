# file tqdm/contrib/logging.py:18-34
# lines [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34]
# branches []

import logging
import pytest
from tqdm import tqdm as std_tqdm
from tqdm.contrib.logging import _TqdmLoggingHandler

class MockTqdm:
    def __init__(self):
        self.messages = []

    def write(self, msg, file=None):
        self.messages.append(msg)

@pytest.fixture
def mock_tqdm():
    return MockTqdm()

@pytest.fixture
def logger(mock_tqdm):
    handler = _TqdmLoggingHandler(tqdm_class=mock_tqdm)
    logger = logging.getLogger("test_logger")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    yield logger
    logger.removeHandler(handler)

def test_emit_normal_message(logger, mock_tqdm):
    logger.info("Test message")
    assert len(mock_tqdm.messages) == 1
    assert "Test message" in mock_tqdm.messages[0]

def test_emit_keyboard_interrupt(logger, mocker):
    mocker.patch.object(_TqdmLoggingHandler, 'format', side_effect=KeyboardInterrupt)
    with pytest.raises(KeyboardInterrupt):
        logger.info("This should raise KeyboardInterrupt")

def test_emit_system_exit(logger, mocker):
    mocker.patch.object(_TqdmLoggingHandler, 'format', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        logger.info("This should raise SystemExit")

def test_emit_generic_exception(logger, mocker, mock_tqdm):
    mocker.patch.object(_TqdmLoggingHandler, 'format', side_effect=Exception("Generic error"))
    logger.info("This should be handled as a generic exception")
    assert len(mock_tqdm.messages) == 0  # No message should be written
