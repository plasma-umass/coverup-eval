# file: pytutils/timers.py:7-29
# asked: {"lines": [], "branches": [[28, 0]]}
# gained: {"lines": [], "branches": [[28, 0]]}

import pytest
import time
import logging
from pytutils.timers import Timer

_LOG = logging.getLogger(__name__)

@pytest.fixture
def mock_time(monkeypatch):
    """Fixture to mock time.time()"""
    mock_time = [0]

    def mock_time_func():
        mock_time[0] += 1
        return mock_time[0]

    monkeypatch.setattr(time, 'time', mock_time_func)
    return mock_time

def test_timer_verbose_logging(mock_time, caplog):
    with caplog.at_level(logging.DEBUG):
        with Timer(name='test', verbose=True) as t:
            pass
    assert 'Elapsed time' in caplog.text
    assert 'test' in caplog.text
    assert 'Elapsed time: 1000.000000 ms' in caplog.text

def test_timer_no_verbose_logging(mock_time, caplog):
    with caplog.at_level(logging.DEBUG):
        with Timer(name='test', verbose=False) as t:
            pass
    assert 'Elapsed time' not in caplog.text
