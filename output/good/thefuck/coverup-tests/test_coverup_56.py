# file thefuck/logs.py:84-90
# lines [84, 85, 86, 87, 88, 90]
# branches []

import pytest
from thefuck.logs import debug_time
from datetime import datetime, timedelta
from unittest.mock import patch

# Test function to cover the debug_time context manager
def test_debug_time(mocker):
    # Mock the debug function to assert it was called with the correct message
    mock_debug = mocker.patch('thefuck.logs.debug')

    # Use the context manager and ensure no exceptions occur within it
    with debug_time("test_message"):
        pass

    # Assert that the debug function was called once
    mock_debug.assert_called_once()

    # Extract the message passed to the debug function
    debug_call_args = mock_debug.call_args[0][0]

    # Assert that the message starts with the correct text
    assert debug_call_args.startswith("test_message took:")

    # Assert that the message contains a timedelta, which means it includes the time taken
    time_taken_str = debug_call_args.split(': ')[1]
    # Parse the time taken string into a timedelta object
    time_taken = datetime.strptime(time_taken_str, '%H:%M:%S.%f') - datetime(1900, 1, 1)
    assert isinstance(time_taken, timedelta)

# Clean up after the test
@pytest.fixture(autouse=True)
def clean_up():
    # Nothing to clean up in this case, but fixture is here for completeness
    yield
    # If there were any global changes, they would be reverted here
