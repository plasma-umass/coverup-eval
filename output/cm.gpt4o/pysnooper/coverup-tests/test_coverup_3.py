# file pysnooper/tracer.py:237-244
# lines [237, 238, 239, 241, 242, 244]
# branches ['238->239', '238->241', '241->242', '241->244']

import pytest
from unittest.mock import patch
import inspect

# Assuming the Tracer class is imported from pysnooper.tracer
from pysnooper.tracer import Tracer

class TestTracer:
    @patch('pysnooper.tracer.DISABLED', False)
    def test_wrap_function(self, mocker):
        tracer = Tracer()

        def sample_function():
            return "sample"

        wrapped_function = tracer(sample_function)
        assert wrapped_function() == "sample"

    @patch('pysnooper.tracer.DISABLED', False)
    def test_wrap_class(self, mocker):
        tracer = Tracer()

        class SampleClass:
            def method(self):
                return "sample"

        wrapped_class = tracer(SampleClass)
        instance = wrapped_class()
        assert instance.method() == "sample"

    @patch('pysnooper.tracer.DISABLED', True)
    def test_disabled(self, mocker):
        tracer = Tracer()

        def sample_function():
            return "sample"

        assert tracer(sample_function) == sample_function

        class SampleClass:
            def method(self):
                return "sample"

        assert tracer(SampleClass) == SampleClass
