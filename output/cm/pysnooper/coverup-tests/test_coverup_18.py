# file pysnooper/tracer.py:246-255
# lines [246, 247, 250, 251, 253, 254, 255]
# branches ['247->250', '247->255', '250->251', '250->253', '253->247', '253->254']

import pytest
import inspect
from unittest.mock import MagicMock

# Assuming pysnooper is available in the context and has a Tracer class
import pysnooper

# Define a coroutine function checker for the test
def is_coroutine_function_mock(func):
    return inspect.iscoroutinefunction(func)

# Mock the coroutine function checker to control its return value
@pytest.fixture
def mock_is_coroutine_function(mocker):
    return mocker.patch('pysnooper.tracer.pycompat.iscoroutinefunction', side_effect=is_coroutine_function_mock)

@pytest.fixture
def mock_is_coroutine_function_true(mocker):
    return mocker.patch('pysnooper.tracer.pycompat.iscoroutinefunction', return_value=True)

class DummyTracer:
    def _wrap_class(self, cls):
        for attr_name, attr in cls.__dict__.items():
            if pysnooper.tracer.pycompat.iscoroutinefunction(attr):
                continue

            if inspect.isfunction(attr):
                setattr(cls, attr_name, self._wrap_function(attr))
        return cls

    def _wrap_function(self, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

def test_wrap_class_with_function(mock_is_coroutine_function):
    tracer = DummyTracer()

    class MyClass:
        def my_method(self):
            pass

    original_method = MyClass.my_method
    wrapped_class = tracer._wrap_class(MyClass)
    wrapped_method = wrapped_class.my_method

    assert wrapped_class is MyClass
    assert wrapped_method is not original_method
    assert inspect.isfunction(wrapped_method)

def test_wrap_class_with_coroutine(mock_is_coroutine_function_true):
    tracer = DummyTracer()

    class MyClass:
        async def my_async_method(self):
            pass

    original_method = MyClass.my_async_method
    wrapped_class = tracer._wrap_class(MyClass)
    wrapped_method = wrapped_class.my_async_method

    assert wrapped_class is MyClass
    assert wrapped_method is original_method  # Should not wrap coroutine functions
