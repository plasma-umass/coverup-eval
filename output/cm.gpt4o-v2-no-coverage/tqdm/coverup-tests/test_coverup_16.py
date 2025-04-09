# file: tqdm/contrib/logging.py:48-98
# asked: {"lines": [48, 49, 50, 51, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98], "branches": [[82, 83], [82, 84], [86, 87], [86, 95], [89, 90], [89, 92], [97, 0], [97, 98]]}
# gained: {"lines": [48, 49, 50, 51, 82, 84, 85, 86, 87, 88, 89, 92, 93, 94, 95, 97, 98], "branches": [[82, 84], [86, 87], [86, 95], [89, 92], [97, 0], [97, 98]]}

import logging
import pytest
from contextlib import contextmanager
from tqdm.std import tqdm as std_tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

class _TqdmLoggingHandler(logging.StreamHandler):
    def __init__(self, tqdm_class=std_tqdm):
        super(_TqdmLoggingHandler, self).__init__()
        self.tqdm_class = tqdm_class

    def emit(self, record):
        self.tqdm_class.write(self.format(record))

def _get_first_found_console_logging_handler(handlers):
    for handler in handlers:
        if _is_console_logging_handler(handler):
            return handler

def _is_console_logging_handler(handler):
    import sys
    return isinstance(handler, logging.StreamHandler) and handler.stream in {sys.stdout, sys.stderr}

@pytest.fixture
def logger():
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    yield logger
    handlers = logger.handlers[:]
    for handler in handlers:
        logger.removeHandler(handler)

def test_logging_redirect_tqdm_default_logger(logger, caplog):
    with logging_redirect_tqdm([logger]):
        logger.info("Test message")
        assert any("Test message" in message for message in caplog.messages)
    assert not any(isinstance(handler, _TqdmLoggingHandler) for handler in logger.handlers)

def test_logging_redirect_tqdm_custom_logger(caplog):
    custom_logger = logging.getLogger('custom_logger')
    custom_logger.setLevel(logging.INFO)
    with logging_redirect_tqdm([custom_logger]):
        custom_logger.info("Test message")
        assert any("Test message" in message for message in caplog.messages)
    assert not any(isinstance(handler, _TqdmLoggingHandler) for handler in custom_logger.handlers)

def test_logging_redirect_tqdm_multiple_loggers(logger, caplog):
    custom_logger = logging.getLogger('custom_logger')
    custom_logger.setLevel(logging.INFO)
    with logging_redirect_tqdm([logger, custom_logger]):
        logger.info("Test message 1")
        custom_logger.info("Test message 2")
        assert any("Test message 1" in message for message in caplog.messages)
        assert any("Test message 2" in message for message in caplog.messages)
    assert not any(isinstance(handler, _TqdmLoggingHandler) for handler in logger.handlers)
    assert not any(isinstance(handler, _TqdmLoggingHandler) for handler in custom_logger.handlers)
