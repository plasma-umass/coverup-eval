# file tqdm/contrib/logging.py:101-128
# lines [123, 124, 125, 126, 127, 128]
# branches []

import logging
from contextlib import contextmanager
from tqdm.contrib.logging import tqdm_logging_redirect
from tqdm import tqdm as std_tqdm
import pytest

# Mocking the logging_redirect_tqdm context manager
@contextmanager
def mock_logging_redirect_tqdm(loggers=None, tqdm_class=None):
    yield

# Test function to cover lines 123-128
@pytest.fixture
def test_logger():
    # Define a custom logger for testing
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    yield logger
    # Clean up by removing the test logger
    logger.handlers.clear()

def test_tqdm_logging_redirect(mocker, test_logger):
    # Mock the logging_redirect_tqdm to ensure it is called correctly
    mock = mocker.patch(
        'tqdm.contrib.logging.logging_redirect_tqdm',
        side_effect=mock_logging_redirect_tqdm
    )

    # Create a list of loggers
    loggers = [test_logger]

    # Use the tqdm_logging_redirect context manager
    with tqdm_logging_redirect(loggers=loggers, tqdm_class=std_tqdm, total=10) as pbar:
        # Perform some updates to simulate progress
        for i in range(10):
            pbar.update(1)

    # Assertions to verify postconditions
    assert pbar.n == 10, "Progress bar did not reach the expected count"
    assert mock.called, "logging_redirect_tqdm was not called"
