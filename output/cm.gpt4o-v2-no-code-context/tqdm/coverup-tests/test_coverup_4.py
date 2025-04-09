# file: tqdm/contrib/logging.py:42-45
# asked: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}
# gained: {"lines": [42, 43, 44, 45], "branches": [[43, 0], [43, 44], [44, 43], [44, 45]]}

import pytest
from unittest.mock import Mock

# Assuming _is_console_logging_handler is defined somewhere in tqdm/contrib/logging.py
from tqdm.contrib.logging import _get_first_found_console_logging_handler, _is_console_logging_handler

def test_get_first_found_console_logging_handler_found(monkeypatch):
    handler1 = Mock()
    handler2 = Mock()
    handler3 = Mock()

    # Mock _is_console_logging_handler to return True for handler2
    monkeypatch.setattr('tqdm.contrib.logging._is_console_logging_handler', lambda h: h == handler2)

    handlers = [handler1, handler2, handler3]
    result = _get_first_found_console_logging_handler(handlers)
    
    assert result == handler2

def test_get_first_found_console_logging_handler_not_found(monkeypatch):
    handler1 = Mock()
    handler2 = Mock()
    handler3 = Mock()

    # Mock _is_console_logging_handler to return False for all handlers
    monkeypatch.setattr('tqdm.contrib.logging._is_console_logging_handler', lambda h: False)

    handlers = [handler1, handler2, handler3]
    result = _get_first_found_console_logging_handler(handlers)
    
    assert result is None
