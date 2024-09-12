# file: pytutils/timers.py:7-29
# asked: {"lines": [7, 8, 12, 13, 14, 16, 17, 19, 20, 21, 23, 24, 25, 26, 28, 29], "branches": [[28, 0], [28, 29]]}
# gained: {"lines": [7, 8, 12, 13, 14, 16, 17, 19, 20, 21, 23, 24, 25, 26, 28, 29], "branches": [[28, 29]]}

import pytest
import time
from pytutils.timers import Timer
import logging

_LOG = logging.getLogger(__name__)

def test_timer_init():
    timer = Timer(name="test", verbose=True)
    assert timer.name == "test"
    assert timer.verbose is True

def test_timer_repr():
    timer = Timer(name="test")
    assert repr(timer) == "Timer(test)"

def test_timer_enter_exit(monkeypatch):
    timer = Timer(verbose=True)
    
    fake_time = [100.0, 105.0]
    def mock_time():
        return fake_time.pop(0)
    
    monkeypatch.setattr(time, 'time', mock_time)
    with monkeypatch.context() as m:
        m.setattr(_LOG, 'debug', lambda *args: None)
        with timer:
            pass
        assert timer.start == 100.0
        assert timer.end == 105.0
        assert timer.secs == 5.0
        assert timer.msecs == 5000.0
