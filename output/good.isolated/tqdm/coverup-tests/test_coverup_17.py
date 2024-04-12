# file tqdm/contrib/logging.py:48-98
# lines [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98]
# branches ['82->83', '82->84', '86->87', '86->95', '89->90', '89->92', '97->exit', '97->98']

import logging
from contextlib import contextmanager
from tqdm.contrib.logging import logging_redirect_tqdm
import pytest

# Assuming _TqdmLoggingHandler, _get_first_found_console_logging_handler, and
# _is_console_logging_handler are defined in the tqdm.contrib.logging module.

class MockTqdm:
    @staticmethod
    def write(msg, file=None, end="\n"):
        print(msg, end=end)

@contextmanager
def mock_tqdm_class():
    yield MockTqdm

@pytest.fixture
def custom_logger():
    # Create a custom logger to test with
    logger = logging.getLogger('test_logger')
    logger.addHandler(logging.StreamHandler())
    yield logger
    # Clean up by removing the custom logger
    logger.handlers = []

def test_logging_redirect_tqdm(custom_logger, mocker):
    # Mock the necessary functions to ensure the branch coverage
    mocker.patch('tqdm.contrib.logging._TqdmLoggingHandler')
    mocker.patch('tqdm.contrib.logging._get_first_found_console_logging_handler', return_value=None)
    mocker.patch('tqdm.contrib.logging._is_console_logging_handler', return_value=False)

    # Store the original handlers to restore later
    original_handlers = custom_logger.handlers[:]

    # Use the context manager to test the branch where loggers is None
    with logging_redirect_tqdm():
        pass

    # Use the context manager with a custom logger and custom tqdm class
    with logging_redirect_tqdm(loggers=[custom_logger], tqdm_class=mock_tqdm_class):
        pass

    # Assertions to check postconditions
    assert custom_logger.handlers == original_handlers, "Handlers should be restored after the context manager"
