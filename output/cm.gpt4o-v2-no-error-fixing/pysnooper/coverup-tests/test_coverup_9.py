# file: pysnooper/tracer.py:237-244
# asked: {"lines": [237, 238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}
# gained: {"lines": [237, 238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}

import pytest
from unittest.mock import patch
import inspect

# Assuming the Tracer class and DISABLED variable are imported from pysnooper.tracer
from pysnooper.tracer import Tracer, DISABLED

@pytest.fixture
def tracer():
    return Tracer()

def test_tracer_call_with_disabled(tracer):
    with patch('pysnooper.tracer.DISABLED', True):
        def sample_function():
            pass
        result = tracer(sample_function)
        assert result is sample_function

def test_tracer_call_with_class(tracer):
    class SampleClass:
        def method(self):
            pass

    with patch('pysnooper.tracer.DISABLED', False), patch.object(tracer, '_wrap_class', return_value='wrapped_class') as mock_wrap_class:
        result = tracer(SampleClass)
        mock_wrap_class.assert_called_once_with(SampleClass)
        assert result == 'wrapped_class'

def test_tracer_call_with_function(tracer):
    def sample_function():
        pass

    with patch('pysnooper.tracer.DISABLED', False), patch.object(tracer, '_wrap_function', return_value='wrapped_function') as mock_wrap_function:
        result = tracer(sample_function)
        mock_wrap_function.assert_called_once_with(sample_function)
        assert result == 'wrapped_function'
