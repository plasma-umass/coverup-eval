# file pysnooper/tracer.py:293-307
# lines [295, 299, 300]
# branches ['294->295', '298->299']

import pytest
import sys
import inspect
from unittest.mock import patch, MagicMock
from pysnooper.tracer import Tracer

@pytest.fixture
def mock_tracer(mocker):
    mocker.patch('pysnooper.tracer.DISABLED', False)
    mocker.patch('pysnooper.tracer.thread_global', MagicMock())
    mocker.patch('pysnooper.tracer.inspect.currentframe', return_value=MagicMock(f_back=MagicMock()))
    mocker.patch('pysnooper.tracer.datetime_module.datetime')
    mocker.patch('pysnooper.tracer.sys.settrace')
    return Tracer()

def test_tracer_enter(mock_tracer, mocker):
    mocker.patch.object(mock_tracer, '_is_internal_frame', return_value=False)
    mocker.patch.object(mock_tracer, 'trace')
    mocker.patch.object(mock_tracer, 'target_frames', set())
    mocker.patch.object(mock_tracer, 'thread_local', MagicMock())
    mocker.patch.object(mock_tracer, 'start_times', {})

    calling_frame = inspect.currentframe().f_back
    mocker.patch('inspect.currentframe', return_value=MagicMock(f_back=calling_frame))

    mock_tracer.__enter__()

    assert calling_frame.f_trace == mock_tracer.trace
    assert calling_frame in mock_tracer.target_frames
    assert sys.gettrace() in mock_tracer.thread_local.__dict__['original_trace_functions']
    assert calling_frame in mock_tracer.start_times

@pytest.fixture(autouse=True)
def cleanup():
    yield
    sys.settrace(None)
