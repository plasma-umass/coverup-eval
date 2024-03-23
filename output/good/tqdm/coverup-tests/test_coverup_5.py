# file tqdm/contrib/logging.py:42-45
# lines [42, 43, 44, 45]
# branches ['43->exit', '43->44', '44->43', '44->45']

import logging
from tqdm.contrib.logging import _get_first_found_console_logging_handler
import pytest

# Assuming the existence of the function _is_console_logging_handler
# which is not provided in the question, we will mock it.

class MockHandler(logging.Handler):
    def __init__(self, is_console_handler):
        super().__init__()
        self.is_console_handler = is_console_handler

    def emit(self, record):
        pass  # MockHandler does not actually emit records

@pytest.fixture
def mock_is_console_logging_handler(mocker):
    return mocker.patch('tqdm.contrib.logging._is_console_logging_handler', side_effect=lambda h: h.is_console_handler)

def test_get_first_found_console_logging_handler(mock_is_console_logging_handler):
    # Create mock handlers
    console_handler = MockHandler(is_console_handler=True)
    non_console_handler = MockHandler(is_console_handler=False)

    # Test with no console handler
    handlers = [non_console_handler, non_console_handler]
    assert _get_first_found_console_logging_handler(handlers) is None

    # Test with one console handler at the beginning
    handlers = [console_handler, non_console_handler]
    assert _get_first_found_console_logging_handler(handlers) is console_handler

    # Test with one console handler in the middle
    handlers = [non_console_handler, console_handler, non_console_handler]
    assert _get_first_found_console_logging_handler(handlers) is console_handler

    # Test with multiple console handlers
    handlers = [non_console_handler, console_handler, console_handler]
    assert _get_first_found_console_logging_handler(handlers) is console_handler

    # Cleanup is handled by pytest's fixture scope
