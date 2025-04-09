# file: tqdm/contrib/logging.py:42-45
# asked: {"lines": [44, 45], "branches": [[43, 44], [44, 43], [44, 45]]}
# gained: {"lines": [44, 45], "branches": [[43, 44], [44, 43], [44, 45]]}

import logging
import sys
import os
import pytest

from tqdm.contrib.logging import _get_first_found_console_logging_handler, _is_console_logging_handler

def test_get_first_found_console_logging_handler_found():
    console_handler = logging.StreamHandler(sys.stdout)
    handlers = [logging.FileHandler('test.log'), console_handler]
    result = _get_first_found_console_logging_handler(handlers)
    assert result is console_handler

def test_get_first_found_console_logging_handler_not_found():
    handlers = [logging.FileHandler('test.log')]
    result = _get_first_found_console_logging_handler(handlers)
    assert result is None

def test_is_console_logging_handler_stdout():
    handler = logging.StreamHandler(sys.stdout)
    assert _is_console_logging_handler(handler) is True

def test_is_console_logging_handler_stderr():
    handler = logging.StreamHandler(sys.stderr)
    assert _is_console_logging_handler(handler) is True

def test_is_console_logging_handler_file():
    handler = logging.FileHandler('test.log')
    assert _is_console_logging_handler(handler) is False

@pytest.fixture(autouse=True)
def cleanup(request):
    def remove_test_log():
        try:
            os.remove('test.log')
        except OSError:
            pass
    request.addfinalizer(remove_test_log)
