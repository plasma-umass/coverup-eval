# file pysnooper/tracer.py:309-326
# lines [311]
# branches ['310->311']

import pytest
from pysnooper.tracer import Tracer
from unittest.mock import patch

@pytest.fixture
def tracer(mocker):
    mocker.patch('pysnooper.tracer.DISABLED', True)
    mocker.patch('sys.settrace')
    mocker.patch('inspect.currentframe')
    mocker.patch('pysnooper.tracer.datetime_module.datetime')
    mocker.patch('pysnooper.tracer.pycompat.timedelta_format')
    t = Tracer()
    t.thread_local.original_trace_functions = []
    t.start_times = {}
    yield t

def test_tracer_exit_with_disabled(tracer):
    with patch.object(tracer, 'write') as mock_write:
        tracer.__exit__(None, None, None)
        mock_write.assert_not_called()
