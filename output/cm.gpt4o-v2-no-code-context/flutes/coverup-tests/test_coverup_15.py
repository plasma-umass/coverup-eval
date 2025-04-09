# file: flutes/timing.py:9-34
# asked: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [9, 10, 30, 31, 32, 33, 34], "branches": []}

import pytest
import time
from flutes.timing import work_in_progress

def test_work_in_progress_function_decorator(monkeypatch):
    # Mock time to control the flow of time
    class MockTime:
        def __init__(self):
            self.current_time = 0

        def time(self):
            return self.current_time

        def sleep(self, seconds):
            self.current_time += seconds

    mock_time = MockTime()
    monkeypatch.setattr(time, 'time', mock_time.time)
    monkeypatch.setattr(time, 'sleep', mock_time.sleep)

    @work_in_progress("Test function")
    def test_func():
        time.sleep(2)
        return "result"

    with monkeypatch.context() as m:
        m.setattr('builtins.print', lambda x, end='', flush=True: None)
        result = test_func()
        assert result == "result"

def test_work_in_progress_context_manager(monkeypatch):
    # Mock time to control the flow of time
    class MockTime:
        def __init__(self):
            self.current_time = 0

        def time(self):
            return self.current_time

        def sleep(self, seconds):
            self.current_time += seconds

    mock_time = MockTime()
    monkeypatch.setattr(time, 'time', mock_time.time)
    monkeypatch.setattr(time, 'sleep', mock_time.sleep)

    with monkeypatch.context() as m:
        m.setattr('builtins.print', lambda x, end='', flush=True: None)
        with work_in_progress("Test context"):
            time.sleep(3)

# Ensure the tests clean up properly
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
