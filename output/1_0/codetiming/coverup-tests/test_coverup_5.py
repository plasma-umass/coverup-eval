# file codetiming/_timer.py:40-65
# lines [40, 42, 43, 46, 47, 50, 51, 52, 54, 55, 56, 57, 58, 60, 61, 62, 63, 65]
# branches ['42->43', '42->46', '50->51', '50->62', '51->52', '51->54', '62->63', '62->65']

import pytest
from codetiming import Timer
from codetiming._timer import TimerError
from unittest.mock import Mock

def test_timer_stop_without_start():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.stop()

def test_timer_stop_with_logger_and_custom_text_function(mocker):
    mock_logger = Mock()
    custom_text_function = lambda x: f"Elapsed time: {x:.2f} seconds"
    timer = Timer(logger=mock_logger, text=custom_text_function)
    mocker.patch('time.perf_counter', return_value=1)  # Simulate 1 second elapsed
    timer._start_time = 0

    elapsed_time = timer.stop()

    assert elapsed_time == 1
    mock_logger.assert_called_once_with("Elapsed time: 1.00 seconds")

def test_timer_stop_with_logger_and_format_string(mocker):
    mock_logger = Mock()
    timer = Timer(logger=mock_logger, text="{seconds:.2f} seconds elapsed")
    mocker.patch('time.perf_counter', return_value=2)  # Simulate 2 seconds elapsed
    timer._start_time = 0

    elapsed_time = timer.stop()

    assert elapsed_time == 2
    mock_logger.assert_called_once_with("2.00 seconds elapsed")

def test_timer_stop_with_name_and_timers_collection(mocker):
    mock_timers_add = Mock()
    timer = Timer(name="test_timer")
    timer.timers = mocker.Mock(add=mock_timers_add)
    mocker.patch('time.perf_counter', return_value=3)  # Simulate 3 seconds elapsed
    timer._start_time = 0

    elapsed_time = timer.stop()

    assert elapsed_time == 3
    mock_timers_add.assert_called_once_with("test_timer", 3)
