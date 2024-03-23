# file codetiming/_timers.py:68-70
# lines [68, 70]
# branches []

import pytest
from codetiming._timers import Timers
from unittest.mock import patch

def test_timers_median_with_empty_values():
    timers = Timers()
    timers.add("test_timer", 0)  # Add a timing with value 0

    with patch("statistics.median", return_value=0) as mock_median:
        result = timers.median("test_timer")

    mock_median.assert_called_once_with([0])
    assert result == 0, "The median of an empty list should return 0"

def test_timers_median_with_non_empty_values():
    timers = Timers()
    timers.add("test_timer", 1)
    timers.add("test_timer", 2)
    timers.add("test_timer", 3)

    with patch("statistics.median", return_value=2) as mock_median:
        result = timers.median("test_timer")

    mock_median.assert_called_once_with([1, 2, 3])
    assert result == 2, "The median of [1, 2, 3] should return 2"
