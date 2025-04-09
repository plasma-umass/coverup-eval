# file: flutes/timing.py:9-34
# asked: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}

import pytest
import time
from flutes.timing import work_in_progress
from io import StringIO
import sys

def test_work_in_progress(monkeypatch):
    # Mock time.time to control the timing
    fake_time = [100.0, 105.0]  # start time, end time
    def mock_time():
        return fake_time.pop(0)
    
    monkeypatch.setattr(time, "time", mock_time)
    
    # Capture the output
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    
    with work_in_progress("Test task"):
        pass  # Simulate a task
    
    # Check the output
    output = captured_output.getvalue().strip()
    assert output == "Test task... done. (5.00s)"
