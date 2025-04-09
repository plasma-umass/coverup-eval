# file: tqdm/contrib/logging.py:18-34
# asked: {"lines": [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34], "branches": []}

import logging
import pytest
from tqdm import tqdm as std_tqdm
from tqdm.contrib.logging import _TqdmLoggingHandler

@pytest.fixture
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    yield logger
    handlers = logger.handlers[:]
    for handler in handlers:
        logger.removeHandler(handler)

def test_tqdm_logging_handler_emit_normal(monkeypatch, caplog, logger):
    handler = _TqdmLoggingHandler(tqdm_class=std_tqdm)
    logger.addHandler(handler)
    
    test_message = "Test log message"
    with caplog.at_level(logging.INFO):
        logger.info(test_message)
    
    assert any(test_message in message for message in caplog.messages)

def test_tqdm_logging_handler_emit_keyboard_interrupt(monkeypatch, logger):
    class MockTqdm:
        @staticmethod
        def write(msg, file=None):
            raise KeyboardInterrupt

    handler = _TqdmLoggingHandler(tqdm_class=MockTqdm)
    logger.addHandler(handler)
    
    with pytest.raises(KeyboardInterrupt):
        logger.info("This should raise KeyboardInterrupt")

def test_tqdm_logging_handler_emit_system_exit(monkeypatch, logger):
    class MockTqdm:
        @staticmethod
        def write(msg, file=None):
            raise SystemExit

    handler = _TqdmLoggingHandler(tqdm_class=MockTqdm)
    logger.addHandler(handler)
    
    with pytest.raises(SystemExit):
        logger.info("This should raise SystemExit")

def test_tqdm_logging_handler_emit_generic_exception(monkeypatch, logger, mocker):
    class MockTqdm:
        @staticmethod
        def write(msg, file=None):
            raise ValueError("Generic exception")

    handler = _TqdmLoggingHandler(tqdm_class=MockTqdm)
    logger.addHandler(handler)
    
    mock_handle_error = mocker.patch.object(handler, 'handleError')
    
    logger.info("This should raise a generic exception")
    
    assert mock_handle_error.called
