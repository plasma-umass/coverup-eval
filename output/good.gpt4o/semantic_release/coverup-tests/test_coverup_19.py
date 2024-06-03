# file semantic_release/helpers.py:42-77
# lines [42, 43, 52, 53, 55, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77]
# branches ['73->74', '73->75']

import pytest
import logging
from unittest.mock import MagicMock
from semantic_release.helpers import LoggedFunction

# Helper function to format arguments
def format_arg(arg):
    return repr(arg)

@pytest.fixture
def mock_logger(mocker):
    return mocker.MagicMock()

def test_logged_function_decorator(mock_logger):
    # Create an instance of the LoggedFunction decorator with the mock logger
    decorator = LoggedFunction(mock_logger)

    # Define a sample function to be decorated
    @decorator
    def sample_function(a, b, c=None):
        return a + b if c is None else a + b + c

    # Call the decorated function
    result = sample_function(1, 2, c=3)

    # Assertions to verify the logger was called with the correct arguments
    mock_logger.debug.assert_any_call("sample_function(1, 2, c=3)")
    mock_logger.debug.assert_any_call("sample_function -> 6")

    # Assert the result of the function call
    assert result == 6

    # Clean up by resetting the mock logger
    mock_logger.reset_mock()
