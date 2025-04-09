# file pysnooper/tracer.py:309-326
# lines [309, 310, 311, 312, 313, 314, 315, 316, 320, 321, 322, 323, 324, 325]
# branches ['310->311', '310->312']

import datetime
import sys
import threading
import pytest
from unittest.mock import Mock
from pysnooper.tracer import Tracer

# Mocking the datetime module to ensure consistent test results
@pytest.fixture
def mock_datetime_module(mocker):
    datetime_mock = mocker.patch('pysnooper.tracer.datetime_module')
    datetime_mock.datetime.now.return_value = datetime.datetime(2021, 1, 1, 12, 0, 0)
    datetime_mock.timedelta_format.return_value = '0:00:00'
    return datetime_mock

# Mocking the pycompat module to ensure consistent test results
@pytest.fixture
def mock_pycompat_module(mocker):
    pycompat_mock = mocker.patch('pysnooper.tracer.pycompat')
    pycompat_mock.timedelta_format.return_value = '0:00:00'
    pycompat_mock.PathLike = str  # Mocking PathLike to be str for isinstance check
    return pycompat_mock

# Mocking the DISABLED constant to ensure the __exit__ method is executed
@pytest.fixture
def mock_DISABLED(mocker):
    mocker.patch('pysnooper.tracer.DISABLED', False)

# Test function to improve coverage
def test_Tracer___exit__(mock_datetime_module, mock_pycompat_module, mock_DISABLED):
    tracer = Tracer(output=Mock())  # Providing a mock for the output parameter
    tracer.start_times = {}
    tracer.thread_local = threading.local()
    tracer.thread_local.original_trace_functions = []
    tracer.target_frames = set()
    tracer.frame_to_local_reprs = {}
    tracer.write = Mock()

    # Simulate entering the context manager to set up the necessary state
    with tracer:
        frame = sys._getframe()
        tracer.start_times[frame] = datetime.datetime(2021, 1, 1, 12, 0, 0)
        tracer.target_frames.add(frame)
        tracer.frame_to_local_reprs[frame] = 'local_repr'
        thread_global = threading.local()
        thread_global.depth = 0

    # Ensure that the write method was called with the correct elapsed time string
    # The expected string should not have leading spaces as the actual call does not include them
    tracer.write.assert_called_with('Elapsed time: 0:00:00')

    # Ensure that the state was cleaned up correctly
    assert frame not in tracer.start_times
    assert frame not in tracer.target_frames
    assert frame not in tracer.frame_to_local_reprs
