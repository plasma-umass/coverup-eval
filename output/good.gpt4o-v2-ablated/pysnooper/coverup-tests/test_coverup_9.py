# file: pysnooper/tracer.py:25-38
# asked: {"lines": [25, 26, 27, 28, 30, 31, 32, 33, 34, 36, 37, 38], "branches": [[36, 37], [36, 38]]}
# gained: {"lines": [25, 26, 27, 28, 30, 31, 32, 33, 34, 36, 37, 38], "branches": [[36, 37], [36, 38]]}

import pytest
import collections
from unittest import mock
from pysnooper import utils

# Mocking utils.get_shortish_repr to return a predictable value
@pytest.fixture
def mock_get_shortish_repr(monkeypatch):
    def mock_repr(value, custom_repr, max_length, normalize):
        return f"repr({value})"
    monkeypatch.setattr(utils, 'get_shortish_repr', mock_repr)

def test_get_local_reprs_basic(mock_get_shortish_repr):
    frame = mock.MagicMock()
    frame.f_code.co_varnames = ('a', 'b')
    frame.f_code.co_cellvars = ('c',)
    frame.f_code.co_freevars = ('d',)
    frame.f_locals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    from pysnooper.tracer import get_local_reprs
    result = get_local_reprs(frame)
    
    expected_keys = ['a', 'b', 'c', 'd', 'e']
    assert list(result.keys()) == expected_keys
    for key in expected_keys:
        assert result[key] == f"repr({frame.f_locals[key]})"

def test_get_local_reprs_with_watch(mock_get_shortish_repr):
    frame = mock.MagicMock()
    frame.f_code.co_varnames = ('a',)
    frame.f_code.co_cellvars = ()
    frame.f_code.co_freevars = ()
    frame.f_locals = {'a': 1}

    watch = [mock.MagicMock()]
    watch[0].items.return_value = [('watched_var', 'watched_value')]

    from pysnooper.tracer import get_local_reprs
    result = get_local_reprs(frame, watch=watch)
    
    assert 'a' in result
    assert result['a'] == "repr(1)"
    assert 'watched_var' in result
    assert result['watched_var'] == 'watched_value'

def test_get_local_reprs_with_custom_repr(mock_get_shortish_repr):
    frame = mock.MagicMock()
    frame.f_code.co_varnames = ('a',)
    frame.f_code.co_cellvars = ()
    frame.f_code.co_freevars = ()
    frame.f_locals = {'a': 1}

    custom_repr = [mock.MagicMock()]
    custom_repr[0].return_value = 'custom_repr'

    from pysnooper.tracer import get_local_reprs
    result = get_local_reprs(frame, custom_repr=custom_repr)
    
    assert 'a' in result
    assert result['a'] == "repr(1)"

def test_get_local_reprs_with_max_length(mock_get_shortish_repr):
    frame = mock.MagicMock()
    frame.f_code.co_varnames = ('a',)
    frame.f_code.co_cellvars = ()
    frame.f_code.co_freevars = ()
    frame.f_locals = {'a': 'a' * 100}

    from pysnooper.tracer import get_local_reprs
    result = get_local_reprs(frame, max_length=10)
    
    assert 'a' in result
    assert result['a'] == "repr(" + 'a' * 100 + ")"

def test_get_local_reprs_with_normalize(mock_get_shortish_repr):
    frame = mock.MagicMock()
    frame.f_code.co_varnames = ('a',)
    frame.f_code.co_cellvars = ()
    frame.f_code.co_freevars = ()
    frame.f_locals = {'a': 1}

    from pysnooper.tracer import get_local_reprs
    result = get_local_reprs(frame, normalize=True)
    
    assert 'a' in result
    assert result['a'] == "repr(1)"
