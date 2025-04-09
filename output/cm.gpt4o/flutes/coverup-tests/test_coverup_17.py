# file flutes/timing.py:9-34
# lines [30, 31, 32, 33, 34]
# branches []

import pytest
import time
from flutes.timing import work_in_progress

def test_work_in_progress(mocker):
    # Mock time.time to control the timing
    mock_time = mocker.patch('time.time', side_effect=[100.0, 105.0])
    
    # Mock print to capture print statements
    mock_print = mocker.patch('builtins.print')
    
    with work_in_progress("Test task"):
        time.sleep(1)  # Simulate some work
    
    # Check that the print statements were called correctly
    mock_print.assert_any_call("Test task... ", end='', flush=True)
    mock_print.assert_any_call("done. (5.00s)")

    # Ensure the time.time was called twice
    assert mock_time.call_count == 2
