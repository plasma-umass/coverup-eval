# file pysnooper/tracer.py:246-255
# lines [247, 250, 251, 253, 254, 255]
# branches ['247->250', '247->255', '250->251', '250->253', '253->247', '253->254']

import pytest
import inspect
from unittest.mock import MagicMock
from pysnooper.tracer import Tracer
from pysnooper import pycompat

# Mocking iscoroutinefunction to force the branch coverage
@pytest.fixture
def mock_iscoroutinefunction(mocker):
    mocker.patch.object(pycompat, 'iscoroutinefunction', return_value=True)

# Test function to cover lines 247-255
def test_wrap_class_with_coroutine(mock_iscoroutinefunction):
    tracer = Tracer()

    class SampleClass:
        def regular_method(self):
            pass

        async def coroutine_method(self):
            pass

    # Before wrapping, coroutine_method should be a coroutine
    assert inspect.iscoroutinefunction(SampleClass.coroutine_method)

    # Wrap the class
    wrapped_cls = tracer._wrap_class(SampleClass)

    # After wrapping, coroutine_method should still be a coroutine
    # and should not be wrapped by the tracer
    assert inspect.iscoroutinefunction(wrapped_cls.coroutine_method)
    assert wrapped_cls.coroutine_method.__name__ == 'coroutine_method'

    # regular_method should be wrapped by the tracer
    assert not inspect.iscoroutinefunction(wrapped_cls.regular_method)
    assert wrapped_cls.regular_method.__name__ == 'regular_method'
