# file: pysnooper/tracer.py:25-38
# asked: {"lines": [31, 37], "branches": [[36, 37]]}
# gained: {"lines": [31, 37], "branches": [[36, 37]]}

import pytest
import collections
from unittest import mock
from pysnooper import tracer
from pysnooper import utils

def test_get_local_reprs_full_coverage(monkeypatch):
    # Mocking frame and its attributes
    mock_frame = mock.MagicMock()
    mock_frame.f_code.co_varnames = ('a', 'b')
    mock_frame.f_code.co_cellvars = ('c',)
    mock_frame.f_code.co_freevars = ('d',)
    mock_frame.f_locals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    # Mocking utils.get_shortish_repr
    def mock_get_shortish_repr(value, custom_repr, max_length, normalize):
        return str(value)
    
    monkeypatch.setattr(utils, 'get_shortish_repr', mock_get_shortish_repr)

    # Mocking a watch variable
    class MockWatch:
        def items(self, frame, normalize):
            return {'e': '6'}.items()
    
    watch = (MockWatch(),)
    
    result = tracer.get_local_reprs(mock_frame, watch=watch)
    
    expected_result = collections.OrderedDict([
        ('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '6')
    ])
    
    assert result == expected_result

