# file: pysnooper/tracer.py:206-235
# asked: {"lines": [206, 207, 208, 209, 211, 212, 213, 214, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235], "branches": [[228, 230], [228, 231]]}
# gained: {"lines": [206, 207, 208, 209, 211, 212, 213, 214, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235], "branches": [[228, 230], [228, 231]]}

import pytest
from pysnooper.tracer import Tracer
from pysnooper.variables import CommonVariable, Exploding
from pysnooper import pycompat
import threading

def test_tracer_init_default():
    tracer = Tracer()
    assert tracer._write is not None
    assert tracer.watch == []
    assert tracer.frame_to_local_reprs == {}
    assert tracer.start_times == {}
    assert tracer.depth == 1
    assert tracer.prefix == ''
    assert tracer.thread_info is False
    assert tracer.thread_info_padding == 0
    assert tracer.target_codes == set()
    assert tracer.target_frames == set()
    assert isinstance(tracer.thread_local, threading.local)
    assert tracer.custom_repr == ()
    assert tracer.last_source_path is None
    assert tracer.max_variable_length == 100
    assert tracer.normalize is False
    assert tracer.relative_time is False

def test_tracer_init_with_params():
    custom_repr = (lambda x: repr(x),)
    tracer = Tracer(output='log.txt', watch=('var1',), watch_explode=('var2',), depth=2,
                    prefix='DEBUG: ', overwrite=True, thread_info=True, custom_repr=custom_repr,
                    max_variable_length=50, normalize=True, relative_time=True)
    assert tracer._write is not None
    assert len(tracer.watch) == 2
    assert isinstance(tracer.watch[0], CommonVariable)
    assert isinstance(tracer.watch[1], Exploding)
    assert tracer.depth == 2
    assert tracer.prefix == 'DEBUG: '
    assert tracer.thread_info is True
    assert tracer.custom_repr == custom_repr
    assert tracer.max_variable_length == 50
    assert tracer.normalize is True
    assert tracer.relative_time is True

def test_tracer_init_custom_repr_tuple():
    custom_repr = (lambda x: repr(x), 'not_iterable')
    tracer = Tracer(custom_repr=custom_repr)
    assert isinstance(tracer.custom_repr, tuple)
    assert len(tracer.custom_repr) == 1
    assert tracer.custom_repr[0] == custom_repr

def test_tracer_init_custom_repr_non_iterable():
    custom_repr = (lambda x: repr(x), 123)
    tracer = Tracer(custom_repr=custom_repr)
    assert isinstance(tracer.custom_repr, tuple)
    assert len(tracer.custom_repr) == 1
    assert tracer.custom_repr[0] == custom_repr

@pytest.fixture
def mock_get_write_function(mocker):
    return mocker.patch('pysnooper.tracer.get_write_function', return_value=lambda x: x)

def test_tracer_init_with_mocked_write_function(mock_get_write_function):
    tracer = Tracer(output='log.txt', overwrite=True)
    mock_get_write_function.assert_called_once_with('log.txt', True)
    assert tracer._write is not None
