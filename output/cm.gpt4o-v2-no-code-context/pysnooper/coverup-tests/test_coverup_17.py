# file: pysnooper/variables.py:20-50
# asked: {"lines": [26, 31, 32, 33, 34, 35, 39, 43, 46, 49, 50], "branches": [[25, 26]]}
# gained: {"lines": [26, 31, 32, 33, 34, 35, 43, 46, 49, 50], "branches": [[25, 26]]}

import pytest
from unittest import mock
from pysnooper.variables import BaseVariable
from pysnooper import pycompat, utils

class TestBaseVariable(BaseVariable):
    def _items(self, key, normalize=False):
        return [(key, normalize)]

@pytest.fixture
def mock_utils(monkeypatch):
    monkeypatch.setattr(utils, 'ensure_tuple', lambda x: (x,) if not isinstance(x, tuple) else x)
    monkeypatch.setattr(pycompat, 'ABC', object)
    yield

def test_needs_parentheses_true(mock_utils, monkeypatch):
    monkeypatch.setattr('pysnooper.variables.needs_parentheses', lambda x: True)
    var = TestBaseVariable('a + b')
    assert var.unambiguous_source == '(a + b)'

def test_needs_parentheses_false(mock_utils, monkeypatch):
    monkeypatch.setattr('pysnooper.variables.needs_parentheses', lambda x: False)
    var = TestBaseVariable('a + b')
    assert var.unambiguous_source == 'a + b'

def test_items_eval_exception(mock_utils):
    var = TestBaseVariable('a + b')
    frame = mock.Mock()
    frame.f_globals = {}
    frame.f_locals = {}
    with mock.patch('builtins.eval', side_effect=Exception):
        assert var.items(frame) == ()

def test_items_normal_execution(mock_utils):
    var = TestBaseVariable('a + b')
    frame = mock.Mock()
    frame.f_globals = {}
    frame.f_locals = {'a': 1, 'b': 2}
    assert var.items(frame) == [(3, False)]

def test_fingerprint_property(mock_utils):
    var = TestBaseVariable('a + b', exclude=('c',))
    assert var._fingerprint == (TestBaseVariable, 'a + b', ('c',))

def test_hash_method(mock_utils):
    var = TestBaseVariable('a + b', exclude=('c',))
    assert hash(var) == hash((TestBaseVariable, 'a + b', ('c',)))

def test_eq_method(mock_utils):
    var1 = TestBaseVariable('a + b', exclude=('c',))
    var2 = TestBaseVariable('a + b', exclude=('c',))
    var3 = TestBaseVariable('a + b', exclude=('d',))
    assert var1 == var2
    assert var1 != var3
    assert var1 != 'not_a_variable'
