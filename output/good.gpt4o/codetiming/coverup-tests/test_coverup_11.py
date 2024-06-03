# file codetiming/_timers.py:68-70
# lines [70]
# branches []

import pytest
from unittest.mock import patch
from codetiming._timers import Timers
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_median_with_no_values(timers):
    timers._timings = {'nonexistent_timer': []}
    with patch('codetiming._timers.statistics.median', return_value=0) as mock_median:
        result = timers.median('nonexistent_timer')
        mock_median.assert_called_once_with([0])
        assert result == 0

def test_median_with_values(timers):
    timers._timings = {'test_timer': [1, 2, 3, 4, 5]}
    result = timers.median('test_timer')
    assert result == 3
