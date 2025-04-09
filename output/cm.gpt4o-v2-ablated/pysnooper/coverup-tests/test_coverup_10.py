# file: pysnooper/tracer.py:237-244
# asked: {"lines": [238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}
# gained: {"lines": [238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}

import pytest
import inspect
from unittest.mock import patch

# Assuming DISABLED and Tracer are imported from pysnooper.tracer

@pytest.fixture
def tracer():
    from pysnooper.tracer import Tracer
    return Tracer()

def test_tracer_disabled(tracer):
    with patch('pysnooper.tracer.DISABLED', True):
        def sample_function():
            return "test"
        result = tracer(sample_function)
        assert result == sample_function

def test_tracer_wrap_class(tracer):
    with patch('pysnooper.tracer.DISABLED', False):
        class SampleClass:
            def method(self):
                return "test"
        result = tracer(SampleClass)
        assert inspect.isclass(result)
        assert result.__name__ == "SampleClass"

def test_tracer_wrap_function(tracer):
    with patch('pysnooper.tracer.DISABLED', False):
        def sample_function():
            return "test"
        result = tracer(sample_function)
        assert callable(result)
        assert result.__name__ == "sample_function"
