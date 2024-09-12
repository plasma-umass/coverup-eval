# file: flutes/timing.py:9-34
# asked: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}

import pytest
import time
from flutes.timing import work_in_progress

def test_work_in_progress_function(monkeypatch):
    # Mock time.time to control the timing
    mock_time = [100.0, 105.0]  # start time, end time
    time_iter = iter(mock_time)
    
    def mock_time_func():
        return next(time_iter)
    
    monkeypatch.setattr(time, 'time', mock_time_func)
    
    # Capture the output
    output = []
    monkeypatch.setattr('sys.stdout.write', lambda x: output.append(x))
    
    with work_in_progress("Test task"):
        pass  # Simulate a task
    
    # Verify the output
    assert ''.join(output) == "Test task... done. (5.00s)\n"

def test_work_in_progress_block(monkeypatch):
    # Mock time.time to control the timing
    mock_time = [200.0, 203.0]  # start time, end time
    time_iter = iter(mock_time)
    
    def mock_time_func():
        return next(time_iter)
    
    monkeypatch.setattr(time, 'time', mock_time_func)
    
    # Capture the output
    output = []
    monkeypatch.setattr('sys.stdout.write', lambda x: output.append(x))
    
    with work_in_progress("Another task"):
        time.sleep(1)  # Simulate a task that takes time
    
    # Verify the output
    assert ''.join(output) == "Another task... done. (3.00s)\n"
