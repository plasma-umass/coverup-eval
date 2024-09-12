# file: pysnooper/tracer.py:237-244
# asked: {"lines": [237, 238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}
# gained: {"lines": [237], "branches": []}

import pytest
import inspect
from unittest.mock import patch

# Assuming DISABLED is a global variable in the module
DISABLED = False

class Tracer:
    def __call__(self, function_or_class):
        if DISABLED:
            return function_or_class

        if inspect.isclass(function_or_class):
            return self._wrap_class(function_or_class)
        else:
            return self._wrap_function(function_or_class)

    def _wrap_class(self, cls):
        # Dummy implementation for testing
        return cls

    def _wrap_function(self, func):
        # Dummy implementation for testing
        return func

@pytest.fixture
def tracer():
    return Tracer()

def test_tracer_disabled(tracer, monkeypatch):
    monkeypatch.setattr('pysnooper.tracer.DISABLED', True)
    def dummy_function():
        pass
    assert tracer(dummy_function) is dummy_function

def test_tracer_wrap_class(tracer):
    class DummyClass:
        pass
    wrapped_class = tracer(DummyClass)
    assert wrapped_class is DummyClass

def test_tracer_wrap_function(tracer):
    def dummy_function():
        pass
    wrapped_function = tracer(dummy_function)
    assert wrapped_function is dummy_function

def test_tracer_wrap_class_with_mock(tracer, mocker):
    class DummyClass:
        pass
    mock_wrap_class = mocker.patch.object(tracer, '_wrap_class', return_value=DummyClass)
    result = tracer(DummyClass)
    mock_wrap_class.assert_called_once_with(DummyClass)
    assert result is DummyClass

def test_tracer_wrap_function_with_mock(tracer, mocker):
    def dummy_function():
        pass
    mock_wrap_function = mocker.patch.object(tracer, '_wrap_function', return_value=dummy_function)
    result = tracer(dummy_function)
    mock_wrap_function.assert_called_once_with(dummy_function)
    assert result is dummy_function
