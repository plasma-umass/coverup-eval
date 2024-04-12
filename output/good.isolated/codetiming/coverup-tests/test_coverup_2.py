# file codetiming/_timers.py:42-46
# lines [42, 44, 45, 46]
# branches ['44->45', '44->46']

import pytest
from codetiming._timers import Timers

def test_timers_apply_with_existing_timer(mocker):
    # Setup
    mock_func = mocker.Mock(return_value=42)
    timers = Timers()
    timers._timings = {"test_timer": [1.0, 2.0, 3.0]}

    # Exercise
    result = timers.apply(mock_func, "test_timer")

    # Verify
    assert result == 42
    mock_func.assert_called_once_with([1.0, 2.0, 3.0])

def test_timers_apply_with_non_existing_timer():
    # Setup
    timers = Timers()
    timers._timings = {}

    # Exercise & Verify
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "non_existing_timer")
