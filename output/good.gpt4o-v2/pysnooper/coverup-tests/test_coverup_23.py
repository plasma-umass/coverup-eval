# file: pysnooper/tracer.py:246-255
# asked: {"lines": [251], "branches": [[250, 251]]}
# gained: {"lines": [251], "branches": [[250, 251]]}

import pytest
import inspect
from pysnooper import pycompat
from pysnooper.tracer import Tracer

class TestTracer:
    def test_wrap_class_with_coroutine(self):
        tracer = Tracer()

        class TestClass:
            async def coro_method(self):
                pass

        wrapped_class = tracer._wrap_class(TestClass)
        
        # Ensure the coroutine method is not wrapped
        assert wrapped_class.coro_method is TestClass.coro_method

    def test_wrap_class_with_regular_function(self, mocker):
        tracer = Tracer()

        class TestClass:
            def regular_method(self):
                pass

        mock_wrap_function = mocker.patch.object(tracer, '_wrap_function', side_effect=lambda x: x)
        wrapped_class = tracer._wrap_class(TestClass)
        
        # Ensure the regular method is wrapped
        assert wrapped_class.regular_method is TestClass.regular_method
        mock_wrap_function.assert_called_once_with(TestClass.regular_method)
