# file: pysnooper/tracer.py:309-326
# asked: {"lines": [311], "branches": [[310, 311]]}
# gained: {"lines": [311], "branches": [[310, 311]]}

import pytest
from unittest.mock import MagicMock, patch
import os
from pysnooper.tracer import Tracer

@pytest.fixture
def tracer():
    tracer = Tracer()
    tracer.thread_local = MagicMock()
    tracer.thread_local.original_trace_functions = [MagicMock()]
    tracer.target_frames = set()
    tracer.frame_to_local_reprs = {}
    tracer.start_times = {}
    return tracer

def test_tracer_exit_with_disabled(tracer):
    with patch.dict(os.environ, {'PYSNOOPER_DISABLED': '1'}):
        with patch('pysnooper.tracer.DISABLED', True):
            tracer.__exit__(None, None, None)
            # Ensure that the function returns early
            assert not tracer.thread_local.original_trace_functions[0].pop.called
            assert not tracer.target_frames
            assert not tracer.frame_to_local_reprs
            assert not tracer.start_times
