# file: apimd/parser.py:36-43
# asked: {"lines": [36, 38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}
# gained: {"lines": [36, 38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}

import pytest
from apimd.parser import _attr

def test_attr_existing_attribute():
    class TestClass:
        def __init__(self):
            self.a = 'value'
    
    obj = TestClass()
    assert _attr(obj, 'a') == 'value'

def test_attr_non_existing_attribute():
    class TestClass:
        def __init__(self):
            self.a = 'value'
    
    obj = TestClass()
    assert _attr(obj, 'b') is None

def test_attr_nested_existing_attribute():
    class InnerClass:
        def __init__(self):
            self.b = 'nested_value'
    
    class TestClass:
        def __init__(self):
            self.a = InnerClass()
    
    obj = TestClass()
    assert _attr(obj, 'a.b') == 'nested_value'

def test_attr_nested_non_existing_attribute():
    class InnerClass:
        def __init__(self):
            self.b = 'nested_value'
    
    class TestClass:
        def __init__(self):
            self.a = InnerClass()
    
    obj = TestClass()
    assert _attr(obj, 'a.c') is None

def test_attr_none_object():
    assert _attr(None, 'a') is None
