# file: pysnooper/variables.py:20-50
# asked: {"lines": [20, 21, 22, 23, 24, 25, 26, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 48, 49, 50], "branches": [[25, 26], [25, 28]]}
# gained: {"lines": [20, 21, 22, 23, 24, 25, 26, 28, 30, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 45, 46, 48, 49, 50], "branches": [[25, 26], [25, 28]]}

import pytest
from pysnooper.variables import BaseVariable, needs_parentheses
from unittest.mock import Mock

class ConcreteVariable(BaseVariable):
    def _items(self, key, normalize=False):
        return [(key, key)]

def test_base_variable_init_with_parentheses(monkeypatch):
    source = "a + b"
    exclude = ("c",)
    mock_utils = Mock()
    mock_utils.ensure_tuple.return_value = exclude
    monkeypatch.setattr("pysnooper.variables.utils", mock_utils)
    monkeypatch.setattr("pysnooper.variables.needs_parentheses", lambda x: True)
    
    var = ConcreteVariable(source, exclude)
    
    assert var.source == source
    assert var.exclude == exclude
    assert var.unambiguous_source == f"({source})"

def test_base_variable_init_without_parentheses(monkeypatch):
    source = "a + b"
    exclude = ("c",)
    mock_utils = Mock()
    mock_utils.ensure_tuple.return_value = exclude
    monkeypatch.setattr("pysnooper.variables.utils", mock_utils)
    monkeypatch.setattr("pysnooper.variables.needs_parentheses", lambda x: False)
    
    var = ConcreteVariable(source, exclude)
    
    assert var.source == source
    assert var.exclude == exclude
    assert var.unambiguous_source == source

def test_base_variable_items(monkeypatch):
    source = "a + b"
    frame = Mock()
    frame.f_globals = {}
    frame.f_locals = {'a': 1, 'b': 2}
    var = ConcreteVariable(source)
    
    items = var.items(frame)
    
    assert items == [(3, 3)]

def test_base_variable_items_exception(monkeypatch):
    source = "a + b"
    frame = Mock()
    frame.f_globals = {}
    frame.f_locals = {}
    var = ConcreteVariable(source)
    
    items = var.items(frame)
    
    assert items == ()

def test_base_variable_fingerprint():
    source = "a + b"
    exclude = ("c",)
    var = ConcreteVariable(source, exclude)
    
    assert var._fingerprint == (ConcreteVariable, source, exclude)

def test_base_variable_hash():
    source = "a + b"
    exclude = ("c",)
    var = ConcreteVariable(source, exclude)
    
    assert hash(var) == hash((ConcreteVariable, source, exclude))

def test_base_variable_eq():
    source = "a + b"
    exclude = ("c",)
    var1 = ConcreteVariable(source, exclude)
    var2 = ConcreteVariable(source, exclude)
    
    assert var1 == var2

def test_base_variable_not_eq():
    source1 = "a + b"
    source2 = "a - b"
    exclude = ("c",)
    var1 = ConcreteVariable(source1, exclude)
    var2 = ConcreteVariable(source2, exclude)
    
    assert var1 != var2
