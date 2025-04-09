# file: tqdm/contrib/logging.py:42-45
# asked: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}
# gained: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}

import logging
import sys
import pytest

from tqdm.contrib.logging import _get_first_found_console_logging_handler, _is_console_logging_handler

def test_get_first_found_console_logging_handler():
    # Create a console logging handler
    console_handler = logging.StreamHandler(sys.stdout)
    # Create a non-console logging handler
    file_handler = logging.FileHandler('test.log')

    handlers = [file_handler, console_handler]

    # Test that the console handler is found
    found_handler = _get_first_found_console_logging_handler(handlers)
    assert found_handler is console_handler

    # Clean up
    file_handler.close()
    console_handler.close()

def test_get_first_found_console_logging_handler_no_console():
    # Create a non-console logging handler
    file_handler = logging.FileHandler('test.log')

    handlers = [file_handler]

    # Test that no console handler is found
    found_handler = _get_first_found_console_logging_handler(handlers)
    assert found_handler is None

    # Clean up
    file_handler.close()
