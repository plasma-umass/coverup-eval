# file: pysnooper/tracer.py:309-326
# asked: {"lines": [311], "branches": [[310, 311]]}
# gained: {"lines": [311], "branches": [[310, 311]]}

import pytest
import sys
import datetime as datetime_module
from unittest.mock import MagicMock, patch
from pysnooper.tracer import Tracer, DISABLED

@pytest.fixture
def tracer():
    return Tracer()

def test_tracer_exit_when_disabled(tracer):
    with patch('pysnooper.tracer.DISABLED', True):
        with patch.object(tracer, 'write') as mock_write:
            tracer.__exit__(None, None, None)
            mock_write.assert_not_called()

def test_tracer_exit(tracer, monkeypatch):
    # Mocking necessary attributes and methods
    mock_stack = MagicMock()
    mock_stack.pop.return_value = None
    mock_thread_local = MagicMock()
    mock_thread_local.original_trace_functions = mock_stack
    mock_currentframe = MagicMock()
    mock_f_back = MagicMock()
    mock_currentframe.return_value.f_back = mock_f_back
    mock_start_time = datetime_module.datetime.now()
    
    monkeypatch.setattr(tracer, 'thread_local', mock_thread_local)
    monkeypatch.setattr(tracer, 'start_times', {mock_f_back: mock_start_time})
    monkeypatch.setattr(tracer, 'write', MagicMock())
    monkeypatch.setattr('inspect.currentframe', mock_currentframe)
    monkeypatch.setattr('sys.settrace', MagicMock())
    monkeypatch.setattr('pysnooper.tracer.thread_global', MagicMock(depth=0))
    monkeypatch.setattr('pysnooper.tracer.pycompat.timedelta_format', lambda x: str(x))

    tracer.target_frames.add(mock_f_back)
    tracer.frame_to_local_reprs[mock_f_back] = None

    tracer.__exit__(None, None, None)

    sys.settrace.assert_called_once_with(None)
    assert mock_f_back not in tracer.target_frames
    assert mock_f_back not in tracer.frame_to_local_reprs
    tracer.write.assert_called_once()
