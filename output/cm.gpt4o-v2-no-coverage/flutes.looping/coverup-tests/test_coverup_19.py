# file: flutes/timing.py:9-34
# asked: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}

import pytest
import time
from flutes.timing import work_in_progress

def test_work_in_progress(monkeypatch, capsys):
    # Mock time.time to control the timing
    fake_time = [100.0, 105.0]  # start time, end time
    def mock_time():
        return fake_time.pop(0)
    
    monkeypatch.setattr(time, 'time', mock_time)
    
    # Execute the context manager
    with work_in_progress("Test task"):
        pass  # Simulate a task
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Verify the output
    assert captured.out == "Test task... done. (5.00s)\n"
