# file: tqdm/contrib/logging.py:42-45
# asked: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}
# gained: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}

import logging
import sys
import pytest
from unittest.mock import MagicMock

from tqdm.contrib.logging import _get_first_found_console_logging_handler, _is_console_logging_handler

def test_get_first_found_console_logging_handler_with_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    handlers = [console_handler]
    
    result = _get_first_found_console_logging_handler(handlers)
    
    assert result is console_handler

def test_get_first_found_console_logging_handler_without_console_handler():
    file_handler = logging.FileHandler('test.log')
    handlers = [file_handler]
    
    result = _get_first_found_console_logging_handler(handlers)
    
    assert result is None

def test_is_console_logging_handler_with_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    
    result = _is_console_logging_handler(console_handler)
    
    assert result is True

def test_is_console_logging_handler_with_non_console_handler():
    file_handler = logging.FileHandler('test.log')
    
    result = _is_console_logging_handler(file_handler)
    
    assert result is False

@pytest.fixture(autouse=True)
def cleanup(request):
    def remove_test_log_file():
        try:
            import os
            os.remove('test.log')
        except OSError:
            pass
    request.addfinalizer(remove_test_log_file)
