# file tqdm/contrib/logging.py:42-45
# lines []
# branches ['43->exit', '44->43']

import pytest
import logging
import sys
from unittest.mock import Mock, patch
from tqdm.contrib.logging import _get_first_found_console_logging_handler

def _is_console_logging_handler(handler):
    return isinstance(handler, logging.StreamHandler) and handler.stream in {sys.stdout, sys.stderr}

@pytest.fixture
def mock_handlers():
    handler1 = Mock(spec=logging.Handler)
    handler2 = logging.StreamHandler(sys.stdout)
    handler3 = logging.StreamHandler(sys.stderr)
    return [handler1, handler2, handler3]

def test_get_first_found_console_logging_handler(mock_handlers):
    with patch('tqdm.contrib.logging._is_console_logging_handler', side_effect=_is_console_logging_handler):
        handler = _get_first_found_console_logging_handler(mock_handlers)
        assert handler is mock_handlers[1]

    # Clean up
    for handler in mock_handlers:
        handler.close()
