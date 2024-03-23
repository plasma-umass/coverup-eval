# file pytutils/timers.py:7-29
# lines [7, 8, 12, 13, 14, 16, 17, 19, 20, 21, 23, 24, 25, 26, 28, 29]
# branches ['28->exit', '28->29']

import time
from pytutils.timers import Timer
import logging
import pytest

# Assuming _LOG is a logger instance in pytutils.timers module
# We need to mock this logger to test the verbose output
@pytest.fixture
def mock_logger(mocker):
    logger = logging.getLogger('pytutils.timers')
    mocker.patch.object(logger, 'debug')
    return logger

def test_timer_verbose_output(mock_logger):
    with Timer(name='test_timer', verbose=True) as t:
        time.sleep(0.1)  # Sleep for a short time to ensure the timer runs

    # Check that the logger was called with the correct message
    mock_logger.debug.assert_called_once()
    call_args = mock_logger.debug.call_args
    assert call_args[0][0] == '%s: Elapsed time: %f ms'
    assert call_args[0][1].name == 'test_timer'
    assert isinstance(call_args[0][2], float)  # Check if the elapsed time is a float

def test_timer_non_verbose_output(mock_logger):
    with Timer(name='test_timer', verbose=False) as t:
        time.sleep(0.1)  # Sleep for a short time to ensure the timer runs

    # Check that the logger was not called
    mock_logger.debug.assert_not_called()

    # Check that the timer has recorded the elapsed time correctly
    assert t.secs >= 0.1
    assert t.msecs >= 100.0
