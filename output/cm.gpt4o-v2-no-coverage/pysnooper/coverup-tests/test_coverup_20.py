# file: pysnooper/variables.py:20-50
# asked: {"lines": [26, 31, 32, 33, 34, 35, 39, 43, 46, 49, 50], "branches": [[25, 26]]}
# gained: {"lines": [26, 31, 32, 33, 34, 35, 43, 46, 49, 50], "branches": [[25, 26]]}

import pytest
from unittest.mock import Mock, patch
from pysnooper.variables import BaseVariable
from pysnooper import utils
import abc

class ConcreteVariable(BaseVariable):
    def _items(self, key, normalize=False):
        return [(key, normalize)]

def test_basevariable_init():
    source = "a + b"
    exclude = ("c", "d")
    with patch('pysnooper.variables.needs_parentheses', return_value=True):
        var = ConcreteVariable(source, exclude)
        assert var.source == source
        assert var.exclude == utils.ensure_tuple(exclude)
        assert var.code is not None
        assert var.unambiguous_source == f"({source})"

    with patch('pysnooper.variables.needs_parentheses', return_value=False):
        var = ConcreteVariable(source, exclude)
        assert var.unambiguous_source == source

def test_basevariable_items():
    source = "a + b"
    frame = Mock()
    frame.f_globals = {'a': 1}
    frame.f_locals = {'b': 2}
    var = ConcreteVariable(source)
    assert var.items(frame) == [(3, False)]

    frame.f_locals = {}
    assert var.items(frame) == ()

def test_basevariable_fingerprint():
    source = "a + b"
    exclude = ("c", "d")
    var = ConcreteVariable(source, exclude)
    assert var._fingerprint == (ConcreteVariable, source, utils.ensure_tuple(exclude))

def test_basevariable_hash():
    source = "a + b"
    exclude = ("c", "d")
    var = ConcreteVariable(source, exclude)
    assert hash(var) == hash((ConcreteVariable, source, utils.ensure_tuple(exclude)))

def test_basevariable_eq():
    source = "a + b"
    exclude = ("c", "d")
    var1 = ConcreteVariable(source, exclude)
    var2 = ConcreteVariable(source, exclude)
    var3 = ConcreteVariable("a - b", exclude)
    assert var1 == var2
    assert var1 != var3
