# file: pysnooper/tracer.py:25-38
# asked: {"lines": [37], "branches": [[36, 37]]}
# gained: {"lines": [37], "branches": [[36, 37]]}

import pytest
import collections
from unittest.mock import Mock

from pysnooper.tracer import get_local_reprs
from pysnooper import utils

@pytest.fixture
def mock_frame():
    frame = Mock()
    frame.f_code = Mock()
    frame.f_code.co_varnames = ('a', 'b')
    frame.f_code.co_cellvars = ('c',)
    frame.f_code.co_freevars = ('d',)
    frame.f_locals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    return frame

def test_get_local_reprs_no_watch_no_custom_repr(mock_frame, monkeypatch):
    def mock_get_shortish_repr(value, custom_repr, max_length, normalize):
        return f"repr({value})"
    
    monkeypatch.setattr(utils, 'get_shortish_repr', mock_get_shortish_repr)
    
    result = get_local_reprs(mock_frame)
    
    expected_order = ['a', 'b', 'c', 'd', 'e']
    assert list(result.keys()) == expected_order
    for key in expected_order:
        assert result[key] == f"repr({mock_frame.f_locals[key]})"

def test_get_local_reprs_with_watch(mock_frame, monkeypatch):
    def mock_get_shortish_repr(value, custom_repr, max_length, normalize):
        return f"repr({value})"
    
    monkeypatch.setattr(utils, 'get_shortish_repr', mock_get_shortish_repr)
    
    mock_watch = [Mock()]
    mock_watch[0].items.return_value = [('f', 'watched_repr')]
    
    result = get_local_reprs(mock_frame, watch=mock_watch)
    
    expected_order = ['a', 'b', 'c', 'd', 'e', 'f']
    assert list(result.keys()) == expected_order
    for key in ['a', 'b', 'c', 'd', 'e']:
        assert result[key] == f"repr({mock_frame.f_locals[key]})"
    assert result['f'] == 'watched_repr'

def test_get_local_reprs_with_custom_repr(mock_frame, monkeypatch):
    def mock_get_shortish_repr(value, custom_repr, max_length, normalize):
        return f"custom_repr({value})" if custom_repr else f"repr({value})"
    
    monkeypatch.setattr(utils, 'get_shortish_repr', mock_get_shortish_repr)
    
    custom_repr = (lambda x: f"custom_repr({x})",)
    
    result = get_local_reprs(mock_frame, custom_repr=custom_repr)
    
    expected_order = ['a', 'b', 'c', 'd', 'e']
    assert list(result.keys()) == expected_order
    for key in expected_order:
        assert result[key] == f"custom_repr({mock_frame.f_locals[key]})"
