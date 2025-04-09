# file: tqdm/contrib/logging.py:42-45
# asked: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}
# gained: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}

import logging
import pytest

from tqdm.contrib.logging import _get_first_found_console_logging_handler

def test_get_first_found_console_logging_handler_found(monkeypatch):
    class MockHandler(logging.Handler):
        def __init__(self, stream=None):
            super().__init__()
            self.stream = stream

    def mock_is_console_logging_handler(handler):
        return handler.stream is not None

    monkeypatch.setattr('tqdm.contrib.logging._is_console_logging_handler', mock_is_console_logging_handler)

    handlers = [MockHandler(), MockHandler(stream='console')]
    result = _get_first_found_console_logging_handler(handlers)
    assert result.stream == 'console'

def test_get_first_found_console_logging_handler_not_found(monkeypatch):
    class MockHandler(logging.Handler):
        def __init__(self, stream=None):
            super().__init__()
            self.stream = stream

    def mock_is_console_logging_handler(handler):
        return handler.stream is not None

    monkeypatch.setattr('tqdm.contrib.logging._is_console_logging_handler', mock_is_console_logging_handler)

    handlers = [MockHandler(), MockHandler()]
    result = _get_first_found_console_logging_handler(handlers)
    assert result is None
