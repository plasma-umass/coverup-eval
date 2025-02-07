# file: pysnooper/tracer.py:25-38
# asked: {"lines": [37], "branches": [[36, 37]]}
# gained: {"lines": [37], "branches": [[36, 37]]}

import pytest
from unittest.mock import Mock
import collections
from pysnooper.tracer import get_local_reprs
from pysnooper.utils import get_shortish_repr

class MockVariable:
    def items(self, frame, normalize):
        return {'mock_key': 'mock_value'}.items()

def test_get_local_reprs_with_watch():
    frame = Mock()
    frame.f_code = Mock()
    frame.f_code.co_varnames = ('a', 'b')
    frame.f_code.co_cellvars = ()
    frame.f_code.co_freevars = ()
    frame.f_locals = {'a': 1, 'b': 2}
    
    watch = [MockVariable()]
    
    result = get_local_reprs(frame, watch=watch)
    
    assert 'mock_key' in result
    assert result['mock_key'] == 'mock_value'

def test_get_local_reprs_without_watch():
    frame = Mock()
    frame.f_code = Mock()
    frame.f_code.co_varnames = ('a', 'b')
    frame.f_code.co_cellvars = ()
    frame.f_code.co_freevars = ()
    frame.f_locals = {'a': 1, 'b': 2}
    
    result = get_local_reprs(frame)
    
    assert 'a' in result
    assert 'b' in result
    assert result['a'] == get_shortish_repr(1)
    assert result['b'] == get_shortish_repr(2)
