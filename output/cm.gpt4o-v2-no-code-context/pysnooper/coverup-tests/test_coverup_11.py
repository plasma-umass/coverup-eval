# file: pysnooper/tracer.py:309-326
# asked: {"lines": [309, 310, 311, 312, 313, 314, 315, 316, 320, 321, 322, 323, 324, 325], "branches": [[310, 311], [310, 312]]}
# gained: {"lines": [309, 310, 311, 312, 313, 314, 315, 316, 320, 321, 322, 323, 324, 325], "branches": [[310, 311], [310, 312]]}

import pytest
import sys
import datetime as datetime_module
import inspect
from unittest.mock import MagicMock, patch

# Assuming the Tracer class is imported from pysnooper.tracer
from pysnooper.tracer import Tracer

class MockThreadLocal:
    def __init__(self):
        self.original_trace_functions = []

class MockThreadGlobal:
    depth = 0

@pytest.fixture
def setup_tracer(monkeypatch):
    tracer = Tracer()
    tracer.thread_local = MockThreadLocal()
    tracer.target_frames = set()
    tracer.frame_to_local_reprs = {}
    tracer.start_times = {}
    
    monkeypatch.setattr('pysnooper.tracer.thread_global', MockThreadGlobal)
    monkeypatch.setattr('pysnooper.tracer.DISABLED', False)
    return tracer

def test_tracer_exit_with_disabled(monkeypatch):
    monkeypatch.setattr('pysnooper.tracer.DISABLED', True)
    tracer = Tracer()
    assert tracer.__exit__(None, None, None) is None

def test_tracer_exit_full_coverage(setup_tracer, monkeypatch):
    tracer = setup_tracer
    mock_frame = MagicMock()
    mock_frame.f_back = mock_frame
    tracer.thread_local.original_trace_functions.append(None)
    tracer.target_frames.add(mock_frame)
    tracer.frame_to_local_reprs[mock_frame] = 'local_repr'
    tracer.start_times[mock_frame] = datetime_module.datetime.now()

    with patch('inspect.currentframe', return_value=mock_frame):
        with patch('pysnooper.tracer.pycompat.timedelta_format', return_value='0:00:00'):
            with patch.object(tracer, 'write') as mock_write:
                tracer.__exit__(None, None, None)
                assert mock_write.called
                assert 'Elapsed time: 0:00:00' in mock_write.call_args[0][0]
                assert mock_frame not in tracer.target_frames
                assert mock_frame not in tracer.frame_to_local_reprs
                assert mock_frame not in tracer.start_times
