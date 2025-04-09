# file tqdm/contrib/logging.py:37-39
# lines [37, 38, 39]
# branches []

import logging
import sys
from tqdm.contrib.logging import _is_console_logging_handler
import pytest

def test_is_console_logging_handler(mocker):
    # Mock sys.stdout and sys.stderr
    mock_stdout = mocker.patch('sys.stdout')
    mock_stderr = mocker.patch('sys.stderr')

    # Test with a StreamHandler to stdout
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    assert _is_console_logging_handler(stdout_handler) is True

    # Test with a StreamHandler to stderr
    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    assert _is_console_logging_handler(stderr_handler) is True

    # Test with a StreamHandler to a different stream
    other_stream_handler = logging.StreamHandler(stream=mocker.Mock())
    assert _is_console_logging_handler(other_stream_handler) is False

    # Test with a different type of handler
    other_handler = logging.Handler()
    assert _is_console_logging_handler(other_handler) is False

    # Clean up by removing the handlers
    logging.getLogger().removeHandler(stdout_handler)
    logging.getLogger().removeHandler(stderr_handler)
    logging.getLogger().removeHandler(other_stream_handler)
    logging.getLogger().removeHandler(other_handler)
