# file: pysnooper/tracer.py:237-244
# asked: {"lines": [237, 238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}
# gained: {"lines": [237, 238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}

import pytest
import inspect
from unittest.mock import patch

# Assuming the Tracer class and necessary imports are available from pysnooper.tracer
from pysnooper.tracer import Tracer

DISABLED = False

class TestTracer:
    @patch('pysnooper.tracer.DISABLED', True)
    def test_call_disabled(self):
        tracer = Tracer()
        
        def sample_function():
            return "sample"
        
        result = tracer(sample_function)
        assert result == sample_function

    @patch('pysnooper.tracer.DISABLED', False)
    def test_call_wrap_function(self):
        tracer = Tracer()
        
        def sample_function():
            return "sample"
        
        wrapped_function = tracer(sample_function)
        assert wrapped_function() == "sample"
        assert wrapped_function.__name__ == "sample_function"

    @patch('pysnooper.tracer.DISABLED', False)
    def test_call_wrap_class(self):
        tracer = Tracer()
        
        class SampleClass:
            def method(self):
                return "method"
        
        wrapped_class = tracer(SampleClass)
        instance = wrapped_class()
        assert instance.method() == "method"
        assert inspect.isclass(wrapped_class)
        assert wrapped_class.__name__ == "SampleClass"

    @patch('pysnooper.tracer.DISABLED', False)
    def test_wrap_class_with_coroutine(self):
        tracer = Tracer()
        
        class SampleClass:
            async def async_method(self):
                return "async_method"
        
        wrapped_class = tracer._wrap_class(SampleClass)
        assert inspect.isclass(wrapped_class)
        assert wrapped_class.__name__ == "SampleClass"
        assert inspect.iscoroutinefunction(wrapped_class.async_method)

    @patch('pysnooper.tracer.DISABLED', False)
    def test_wrap_function_generator(self):
        tracer = Tracer()
        
        def sample_generator():
            yield "step1"
            yield "step2"
        
        wrapped_generator = tracer._wrap_function(sample_generator)
        gen = wrapped_generator()
        assert next(gen) == "step1"
        assert next(gen) == "step2"

    @patch('pysnooper.tracer.DISABLED', False)
    def test_wrap_function_simple(self):
        tracer = Tracer()
        
        def sample_function():
            return "sample"
        
        wrapped_function = tracer._wrap_function(sample_function)
        assert wrapped_function() == "sample"
        assert wrapped_function.__name__ == "sample_function"
