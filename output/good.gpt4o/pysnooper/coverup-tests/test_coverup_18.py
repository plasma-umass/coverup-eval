# file pysnooper/tracer.py:309-326
# lines [311]
# branches ['310->311']

import pytest
from unittest import mock
import sys
import datetime as datetime_module
import inspect
from pysnooper.tracer import Tracer

# Mocking the DISABLED variable
DISABLED = True

@pytest.fixture
def mock_tracer():
    tracer = Tracer()
    tracer.thread_local = mock.Mock()
    tracer.thread_local.original_trace_functions = []
    tracer.target_frames = set()
    tracer.frame_to_local_reprs = {}
    tracer.start_times = {}
    return tracer

def test_tracer_exit_disabled(mock_tracer):
    with mock.patch('pysnooper.tracer.DISABLED', True):
        mock_tracer.__exit__(None, None, None)
        # Assert that the function returns early when DISABLED is True
        assert True  # If we reach here, it means the early return worked

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Reset the DISABLED variable to its original state
    global DISABLED
    DISABLED = False
