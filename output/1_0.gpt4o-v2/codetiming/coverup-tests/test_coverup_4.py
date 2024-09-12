# file: codetiming/_timer.py:40-65
# asked: {"lines": [43, 52, 63], "branches": [[42, 43], [50, 62], [51, 52], [62, 63]]}
# gained: {"lines": [43, 52, 63], "branches": [[42, 43], [51, 52], [62, 63]]}

import pytest
from codetiming import Timer, TimerError
import time
import re

def test_timer_stop_not_running():
    timer = Timer()
    with pytest.raises(TimerError, match=re.escape("Timer is not running. Use .start() to start it")):
        timer.stop()

def test_timer_stop_with_callable_text(mocker):
    mock_logger = mocker.Mock()
    mock_text = mocker.Mock(return_value="Elapsed time: 1.0 seconds")
    timer = Timer(logger=mock_logger, text=mock_text)
    timer._start_time = time.perf_counter() - 1.0
    timer.stop()
    mock_text.assert_called_once_with(timer.last)
    mock_logger.assert_called_once_with("Elapsed time: 1.0 seconds")

def test_timer_stop_with_formatted_text(mocker):
    mock_logger = mocker.Mock()
    timer = Timer(logger=mock_logger, text="Elapsed time: {seconds:.2f} seconds", name="test_timer")
    timer._start_time = time.perf_counter() - 1.0
    timer.stop()
    mock_logger.assert_called_once_with("Elapsed time: 1.00 seconds")

def test_timer_stop_with_name(mocker):
    mock_timers = mocker.Mock()
    timer = Timer(name="test_timer")
    timer.timers = mock_timers
    timer._start_time = time.perf_counter() - 1.0
    timer.stop()
    mock_timers.add.assert_called_once_with("test_timer", timer.last)
