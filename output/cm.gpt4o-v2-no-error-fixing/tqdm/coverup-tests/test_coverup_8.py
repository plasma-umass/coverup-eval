# file: tqdm/contrib/logging.py:101-128
# asked: {"lines": [101, 102, 123, 124, 125, 126, 127, 128], "branches": []}
# gained: {"lines": [101, 102, 123, 124, 125, 126, 127, 128], "branches": []}

import pytest
import logging
from tqdm import trange
from tqdm.contrib.logging import tqdm_logging_redirect

def test_tqdm_logging_redirect_default():
    log_message = "console logging redirected to `tqdm.write()`"
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    with tqdm_logging_redirect(total=9) as pbar:
        for i in range(9):
            if i == 4:
                logger.info(log_message)
            pbar.update(1)
    assert True  # If no exceptions, the test passes

def test_tqdm_logging_redirect_custom_logger():
    log_message = "console logging redirected to `tqdm.write()`"
    custom_logger = logging.getLogger('custom_logger')
    custom_logger.setLevel(logging.INFO)
    with tqdm_logging_redirect(total=9, loggers=[custom_logger]) as pbar:
        for i in range(9):
            if i == 4:
                custom_logger.info(log_message)
            pbar.update(1)
    assert True  # If no exceptions, the test passes

def test_tqdm_logging_redirect_custom_tqdm_class(monkeypatch):
    class CustomTqdm:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.n = 0

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def update(self, n):
            self.n += n

    log_message = "console logging redirected to `tqdm.write()`"
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    with tqdm_logging_redirect(total=9, tqdm_class=CustomTqdm) as pbar:
        for i in range(9):
            if i == 4:
                logger.info(log_message)
            pbar.update(1)
    assert pbar.n == 9  # Ensure the custom tqdm class was used and updated correctly
