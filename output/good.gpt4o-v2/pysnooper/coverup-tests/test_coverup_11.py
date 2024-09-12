# file: pysnooper/tracer.py:257-287
# asked: {"lines": [257, 258, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 280, 281, 282, 283, 284, 285, 287], "branches": [[269, 270], [280, 281], [280, 282], [282, 283], [282, 284], [284, 285], [284, 287]]}
# gained: {"lines": [257, 258, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 272, 275, 276, 277, 280, 281, 282, 283, 284, 285, 287], "branches": [[269, 270], [280, 281], [280, 282], [282, 283], [282, 284], [284, 285], [284, 287]]}

import pytest
import functools
import inspect
from pysnooper import pycompat
from pysnooper.tracer import Tracer

@pytest.fixture
def tracer():
    return Tracer()

def test_wrap_function_simple(tracer):
    def simple_function(x, y):
        return x + y

    wrapped_function = tracer._wrap_function(simple_function)
    assert wrapped_function(2, 3) == 5

def test_wrap_function_generator(tracer):
    def generator_function(x):
        yield x
        yield x + 1

    wrapped_function = tracer._wrap_function(generator_function)
    gen = wrapped_function(2)
    assert next(gen) == 2
    assert next(gen) == 3

def test_wrap_function_coroutine(tracer, monkeypatch):
    def coroutine_function(x):
        return x

    monkeypatch.setattr(pycompat, 'iscoroutinefunction', lambda func: True)
    with pytest.raises(NotImplementedError):
        tracer._wrap_function(coroutine_function)

def test_wrap_function_asyncgen(tracer, monkeypatch):
    def asyncgen_function(x):
        yield x

    monkeypatch.setattr(pycompat, 'isasyncgenfunction', lambda func: True)
    with pytest.raises(NotImplementedError):
        tracer._wrap_function(asyncgen_function)
