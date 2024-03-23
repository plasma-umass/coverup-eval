# file codetiming/_timer.py:33-38
# lines [33, 35, 36, 38]
# branches ['35->36', '35->38']

import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_timer_start_when_already_started(mocker):
    mocker.patch('time.perf_counter', return_value=123.456)
    timer = Timer()
    timer.start()  # Start the timer for the first time

    with pytest.raises(TimerError) as exc_info:
        timer.start()  # Attempt to start the timer again without stopping should raise TimerError

    assert str(exc_info.value) == "Timer is running. Use .stop() to stop it"
    assert timer._start_time == 123.456  # Ensure the start time was set by the first start call
