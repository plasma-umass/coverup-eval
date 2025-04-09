# file pysnooper/tracer.py:309-326
# lines [309, 310, 311, 312, 313, 314, 315, 316, 320, 321, 322, 323, 324, 325]
# branches ['310->311', '310->312']

import pytest
import sys
import inspect
import datetime as datetime_module
from unittest import mock
from pysnooper.tracer import Tracer

@pytest.fixture
def mock_sys_settrace(mocker):
    return mocker.patch('sys.settrace')

@pytest.fixture
def mock_datetime_now(mocker):
    class MockDateTime(datetime_module.datetime):
        @classmethod
        def now(cls):
            return datetime_module.datetime(2023, 1, 1, 12, 0, 0)
    return mocker.patch('datetime.datetime', MockDateTime)

@pytest.fixture
def mock_pycompat_timedelta_format(mocker):
    return mocker.patch('pysnooper.pycompat.timedelta_format', return_value='0:00:01')

@pytest.fixture
def tracer_instance():
    tracer = Tracer()
    tracer.thread_local = mock.Mock()
    tracer.thread_local.original_trace_functions = [None]
    tracer.target_frames = set()
    tracer.frame_to_local_reprs = {}
    tracer.start_times = {}
    return tracer

def test_tracer_exit(mock_sys_settrace, mock_datetime_now, mock_pycompat_timedelta_format, tracer_instance):
    calling_frame = inspect.currentframe()
    tracer_instance.start_times[calling_frame] = datetime_module.datetime(2023, 1, 1, 11, 59, 59)
    
    with mock.patch('pysnooper.tracer.thread_global', mock.Mock(depth=0)):
        with mock.patch.object(tracer_instance, 'write') as mock_write:
            tracer_instance.__exit__(None, None, None)
            
            mock_sys_settrace.assert_called_once_with(None)
            assert calling_frame not in tracer_instance.target_frames
            assert calling_frame not in tracer_instance.frame_to_local_reprs
            assert calling_frame not in tracer_instance.start_times
            mock_write.assert_called_once_with('    Elapsed time: 0:00:01')
