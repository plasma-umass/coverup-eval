# file codetiming/_timers.py:56-58
# lines [56, 58]
# branches []

import pytest
from unittest.mock import MagicMock
from codetiming._timers import Timers

@pytest.fixture
def mock_timers():
    timers = Timers()
    timers.apply = MagicMock()
    return timers

def test_timers_min(mock_timers):
    # Test with no timings
    mock_timers.apply.return_value = 0
    assert mock_timers.min("test_timer") == 0
    assert mock_timers.apply.call_count == 1
    assert mock_timers.apply.call_args[1]['name'] == "test_timer"
    
    # Test with some timings
    mock_timers.apply.reset_mock()
    mock_timers.apply.return_value = 1.23
    assert mock_timers.min("test_timer") == 1.23
    assert mock_timers.apply.call_count == 1
    assert mock_timers.apply.call_args[1]['name'] == "test_timer"
