# file: tqdm/contrib/logging.py:48-98
# asked: {"lines": [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98], "branches": [[82, 83], [82, 84], [86, 87], [86, 95], [89, 90], [89, 92], [97, 0], [97, 98]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98], "branches": [[82, 83], [82, 84], [86, 87], [86, 95], [89, 90], [89, 92], [97, 0], [97, 98]]}

import logging
import pytest
from tqdm import trange
from tqdm.contrib.logging import logging_redirect_tqdm

class _TqdmLoggingHandler(logging.Handler):
    def __init__(self, tqdm_class):
        super().__init__()
        self.tqdm_class = tqdm_class

    def emit(self, record):
        try:
            msg = self.format(record)
            self.tqdm_class.write(msg)
        except Exception:
            self.handleError(record)

def _get_first_found_console_logging_handler(handlers):
    for handler in handlers:
        if _is_console_logging_handler(handler):
            return handler
    return None

def _is_console_logging_handler(handler):
    return isinstance(handler, logging.StreamHandler) and handler.stream in {sys.stdout, sys.stderr}

@pytest.fixture
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    yield logger
    logger.removeHandler(stream_handler)

def test_logging_redirect_tqdm_default_logger(setup_logging):
    logger = setup_logging
    with logging_redirect_tqdm():
        for i in trange(3):
            if i == 1:
                logger.info("Test message")
    assert True  # If no exceptions, the test passes

def test_logging_redirect_tqdm_custom_logger(setup_logging):
    logger = setup_logging
    with logging_redirect_tqdm([logger]):
        for i in trange(3):
            if i == 1:
                logger.info("Test message")
    assert True  # If no exceptions, the test passes

def test_logging_redirect_tqdm_no_console_handler(monkeypatch):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('/dev/null')
    logger.addHandler(file_handler)
    
    with logging_redirect_tqdm([logger]):
        for i in trange(3):
            if i == 1:
                logger.info("Test message")
    
    logger.removeHandler(file_handler)
    assert True  # If no exceptions, the test passes
