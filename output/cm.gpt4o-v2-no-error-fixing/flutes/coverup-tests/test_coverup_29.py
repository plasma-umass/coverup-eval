# file: flutes/timing.py:9-34
# asked: {"lines": [30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [30, 31, 32, 33, 34], "branches": []}

import pytest
from flutes.timing import work_in_progress
import time

def test_work_in_progress(capsys):
    with work_in_progress("Test task"):
        time.sleep(1)
    
    captured = capsys.readouterr()
    assert "Test task... " in captured.out
    assert "done. (1.00" in captured.out or "done. (1.01" in captured.out

