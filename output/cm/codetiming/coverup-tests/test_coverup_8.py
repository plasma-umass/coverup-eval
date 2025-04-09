# file codetiming/_timers.py:48-50
# lines [50]
# branches []

import pytest
from unittest.mock import MagicMock
from codetiming._timers import Timers

@pytest.fixture
def mock_timers():
    timers = Timers()
    timers.data = MagicMock()
    return timers

def test_timers_count(mock_timers):
    # Setup a mock for the 'apply' method
    mock_timers.apply = MagicMock(return_value=3)
    timer_name = "test_timer"

    # Call the 'count' method which should in turn call 'apply'
    count = mock_timers.count(timer_name)

    # Assert that 'apply' was called with the correct arguments
    mock_timers.apply.assert_called_once_with(len, name=timer_name)

    # Assert that the return value is as expected
    assert count == 3
