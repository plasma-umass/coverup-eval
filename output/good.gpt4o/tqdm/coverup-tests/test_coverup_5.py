# file tqdm/contrib/logging.py:37-39
# lines [37, 38, 39]
# branches []

import logging
import sys
import os
import pytest

from tqdm.contrib.logging import _is_console_logging_handler

def test_is_console_logging_handler_stdout(mocker):
    handler = logging.StreamHandler(sys.stdout)
    assert _is_console_logging_handler(handler) == True

def test_is_console_logging_handler_stderr(mocker):
    handler = logging.StreamHandler(sys.stderr)
    assert _is_console_logging_handler(handler) == True

def test_is_console_logging_handler_other_stream(mocker):
    mock_stream = mocker.Mock()
    handler = logging.StreamHandler(mock_stream)
    assert _is_console_logging_handler(handler) == False

def test_is_console_logging_handler_non_stream_handler(mocker):
    handler = logging.FileHandler('test.log')
    assert _is_console_logging_handler(handler) == False

@pytest.fixture(autouse=True)
def cleanup():
    yield
    try:
        os.remove('test.log')
    except FileNotFoundError:
        pass
