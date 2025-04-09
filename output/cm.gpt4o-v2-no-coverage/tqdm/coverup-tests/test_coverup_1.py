# file: tqdm/contrib/logging.py:37-39
# asked: {"lines": [37, 38, 39], "branches": []}
# gained: {"lines": [37, 38, 39], "branches": []}

import logging
import sys
import pytest

from tqdm.contrib.logging import _is_console_logging_handler

def test_is_console_logging_handler_stdout():
    handler = logging.StreamHandler(sys.stdout)
    assert _is_console_logging_handler(handler) == True

def test_is_console_logging_handler_stderr():
    handler = logging.StreamHandler(sys.stderr)
    assert _is_console_logging_handler(handler) == True

def test_is_console_logging_handler_other_stream():
    import io
    handler = logging.StreamHandler(io.StringIO())
    assert _is_console_logging_handler(handler) == False

def test_is_console_logging_handler_non_stream_handler():
    handler = logging.FileHandler('test.log')
    assert _is_console_logging_handler(handler) == False
    handler.close()
    import os
    os.remove('test.log')
