# file: tqdm/contrib/logging.py:101-128
# asked: {"lines": [101, 102, 123, 124, 125, 126, 127, 128], "branches": []}
# gained: {"lines": [101, 102, 123, 124, 125, 126, 127, 128], "branches": []}

import pytest
import logging
from tqdm.contrib.logging import tqdm_logging_redirect
from tqdm import tqdm

def test_tqdm_logging_redirect_default():
    with tqdm_logging_redirect(total=3) as pbar:
        for _ in range(3):
            pbar.update(1)
    assert pbar.n == 3

def test_tqdm_logging_redirect_custom_logger():
    custom_logger = logging.getLogger("custom_logger")
    with tqdm_logging_redirect(total=3, loggers=[custom_logger]) as pbar:
        for _ in range(3):
            pbar.update(1)
    assert pbar.n == 3

def test_tqdm_logging_redirect_custom_tqdm_class():
    class CustomTqdm(tqdm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.custom_attr = True

    with tqdm_logging_redirect(total=3, tqdm_class=CustomTqdm) as pbar:
        for _ in range(3):
            pbar.update(1)
    assert pbar.n == 3
    assert hasattr(pbar, 'custom_attr')
