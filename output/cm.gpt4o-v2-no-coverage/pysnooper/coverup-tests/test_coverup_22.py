# file: pysnooper/tracer.py:206-235
# asked: {"lines": [212, 215, 229, 230], "branches": [[228, 230]]}
# gained: {"lines": [212, 215, 229, 230], "branches": [[228, 230]]}

import pytest
from pysnooper.tracer import Tracer
from pysnooper.variables import CommonVariable, Exploding, BaseVariable
from pysnooper import utils, pycompat
import threading

def test_tracer_init_with_defaults():
    tracer = Tracer()
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info is False
    assert tracer.custom_repr == ()
    assert tracer.max_variable_length == 100
    assert tracer.normalize is False
    assert tracer.relative_time is False

def test_tracer_init_with_custom_values():
    custom_repr = (lambda x: repr(x),)
    tracer = Tracer(output='log.txt', watch=('var1',), watch_explode=('var2',), depth=2,
                    prefix='DEBUG: ', overwrite=True, thread_info=True, custom_repr=custom_repr,
                    max_variable_length=200, normalize=True, relative_time=True)
    assert tracer.depth == 2
    assert tracer.prefix == 'DEBUG: '
    assert tracer.thread_info is True
    assert tracer.custom_repr == custom_repr
    assert tracer.max_variable_length == 200
    assert tracer.normalize is True
    assert tracer.relative_time is True

def test_tracer_init_with_invalid_custom_repr():
    custom_repr = (lambda x: repr(x), 123)
    tracer = Tracer(custom_repr=custom_repr)
    assert tracer.custom_repr == (custom_repr,)

def test_tracer_init_watch_and_watch_explode():
    watch = ('var1',)
    watch_explode = ('var2',)
    tracer = Tracer(watch=watch, watch_explode=watch_explode)
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], CommonVariable)
    assert isinstance(tracer.watch[1], Exploding)

def test_tracer_init_thread_local():
    tracer = Tracer()
    assert isinstance(tracer.thread_local, threading.local)

def test_tracer_init_write_function(monkeypatch):
    def mock_get_write_function(output, overwrite):
        return lambda s: None

    monkeypatch.setattr('pysnooper.tracer.get_write_function', mock_get_write_function)
    tracer = Tracer(output='log.txt', overwrite=True)
    assert callable(tracer._write)
