# file: pysnooper/tracer.py:237-244
# asked: {"lines": [237, 238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}
# gained: {"lines": [237, 238, 239, 241, 242, 244], "branches": [[238, 239], [238, 241], [241, 242], [241, 244]]}

import pytest
from unittest import mock
import inspect
from pysnooper.tracer import Tracer

class DummyClass:
    def method(self):
        pass

def dummy_function():
    pass

@pytest.fixture
def tracer():
    return Tracer()

def test_tracer_disabled(monkeypatch, tracer):
    monkeypatch.setattr('pysnooper.tracer.DISABLED', True)
    assert tracer(dummy_function) is dummy_function

def test_tracer_wrap_class(tracer):
    with mock.patch.object(tracer, '_wrap_class', return_value='wrapped_class') as mock_wrap_class:
        result = tracer(DummyClass)
        mock_wrap_class.assert_called_once_with(DummyClass)
        assert result == 'wrapped_class'

def test_tracer_wrap_function(tracer):
    with mock.patch.object(tracer, '_wrap_function', return_value='wrapped_function') as mock_wrap_function:
        result = tracer(dummy_function)
        mock_wrap_function.assert_called_once_with(dummy_function)
        assert result == 'wrapped_function'
