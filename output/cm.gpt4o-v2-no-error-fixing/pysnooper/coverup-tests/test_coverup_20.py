# file: pysnooper/tracer.py:257-287
# asked: {"lines": [273, 274, 278], "branches": []}
# gained: {"lines": [273, 274], "branches": []}

import pytest
from unittest import mock
from pysnooper.tracer import Tracer

def test_wrap_function_generator_stop_iteration():
    tracer = Tracer()
    tracer.target_codes = set()

    def generator_function():
        yield 1
        return

    wrapped_function = tracer._wrap_function(generator_function)
    gen = wrapped_function()

    assert next(gen) == 1
    with pytest.raises(StopIteration):
        next(gen)

def test_wrap_function_generator_exception():
    tracer = Tracer()
    tracer.target_codes = set()

    def generator_function():
        yield 1
        raise ValueError("Test exception")

    wrapped_function = tracer._wrap_function(generator_function)
    gen = wrapped_function()

    assert next(gen) == 1
    with pytest.raises(ValueError, match="Test exception"):
        next(gen)

@pytest.fixture
def mock_pycompat(monkeypatch):
    monkeypatch.setattr('pysnooper.pycompat.iscoroutinefunction', lambda func: False)
    monkeypatch.setattr('pysnooper.pycompat.isasyncgenfunction', lambda func: False)

def test_wrap_function_simple_function(mock_pycompat):
    tracer = Tracer()
    tracer.target_codes = set()

    def simple_function():
        return "test"

    wrapped_function = tracer._wrap_function(simple_function)
    assert wrapped_function() == "test"
