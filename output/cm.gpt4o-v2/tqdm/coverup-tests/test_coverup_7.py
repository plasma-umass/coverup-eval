# file: tqdm/contrib/logging.py:18-34
# asked: {"lines": [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34], "branches": []}

import logging
import pytest
from tqdm.std import tqdm as std_tqdm
from tqdm.contrib.logging import _TqdmLoggingHandler

@pytest.fixture
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    yield logger
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

def test_tqdm_logging_handler_init():
    handler = _TqdmLoggingHandler()
    assert handler.tqdm_class == std_tqdm

def test_tqdm_logging_handler_emit(logger, mocker):
    handler = _TqdmLoggingHandler()
    logger.addHandler(handler)
    mock_write = mocker.patch.object(std_tqdm, 'write')
    mock_flush = mocker.patch.object(handler, 'flush')

    logger.info("Test message")
    assert mock_write.called
    assert mock_flush.called

def test_tqdm_logging_handler_emit_keyboard_interrupt(logger, mocker):
    handler = _TqdmLoggingHandler()
    logger.addHandler(handler)
    mocker.patch.object(handler, 'format', side_effect=KeyboardInterrupt)

    with pytest.raises(KeyboardInterrupt):
        logger.info("Test message")

def test_tqdm_logging_handler_emit_system_exit(logger, mocker):
    handler = _TqdmLoggingHandler()
    logger.addHandler(handler)
    mocker.patch.object(handler, 'format', side_effect=SystemExit)

    with pytest.raises(SystemExit):
        logger.info("Test message")

def test_tqdm_logging_handler_emit_generic_exception(logger, mocker):
    handler = _TqdmLoggingHandler()
    logger.addHandler(handler)
    mock_handle_error = mocker.patch.object(handler, 'handleError')
    mocker.patch.object(handler, 'format', side_effect=Exception)

    logger.info("Test message")
    assert mock_handle_error.called
