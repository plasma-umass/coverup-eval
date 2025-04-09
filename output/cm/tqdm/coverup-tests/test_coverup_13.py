# file tqdm/contrib/logging.py:18-34
# lines [18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34]
# branches []

import logging
from tqdm.contrib.logging import _TqdmLoggingHandler
from tqdm import tqdm
import pytest
from unittest.mock import Mock, patch

# Define a test function to cover the missing lines/branches
@pytest.fixture
def logger():
    # Create a logger and attach the _TqdmLoggingHandler
    logger = logging.getLogger('test_tqdm_logging_handler_emit_exception')
    tqdm_handler = _TqdmLoggingHandler(tqdm_class=tqdm)
    logger.addHandler(tqdm_handler)
    logger.setLevel(logging.INFO)
    yield logger
    logger.removeHandler(tqdm_handler)

def test_tqdm_logging_handler_emit_exception(mocker, logger):
    # Mock tqdm.write to raise an exception when called
    mock_tqdm_write = mocker.patch('tqdm.std.tqdm.write', side_effect=Exception("Test exception"))

    # Mock the handleError method to track if it's called
    mock_handle_error = mocker.patch.object(_TqdmLoggingHandler, 'handleError')

    # Emit a log record
    logger.error('test message')

    # Assert that tqdm.write raised an exception and handleError was called
    assert mock_tqdm_write.call_count == 1
    mock_handle_error.assert_called_once()

# This is just to demonstrate how the test function would be called in a test suite,
# it should not be included in the top-level code.
if __name__ == "__main__":
    pytest.main()
