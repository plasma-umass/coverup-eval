# file: apimd/parser.py:36-43
# asked: {"lines": [36, 38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}
# gained: {"lines": [36, 38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}

import pytest
from apimd.parser import _attr

class Dummy:
    def __init__(self):
        self.a = 'value'
        self.b = DummyB()

class DummyB:
    def __init__(self):
        self.c = 'nested_value'

def test_attr_direct_attribute():
    obj = Dummy()
    assert _attr(obj, 'a') == 'value'

def test_attr_nested_attribute():
    obj = Dummy()
    assert _attr(obj, 'b.c') == 'nested_value'

def test_attr_non_existent_attribute():
    obj = Dummy()
    assert _attr(obj, 'd') is None

def test_attr_partial_non_existent_nested_attribute():
    obj = Dummy()
    assert _attr(obj, 'b.d') is None

def test_attr_empty_string():
    obj = Dummy()
    assert _attr(obj, '') is None
