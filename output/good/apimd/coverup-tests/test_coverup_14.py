# file apimd/parser.py:36-43
# lines [36, 38, 39, 40, 41, 42, 43]
# branches ['39->40', '39->43', '41->39', '41->42']

import pytest
from apimd.parser import _attr

class MockObject:
    def __init__(self):
        self.nested = NestedObject()

class NestedObject:
    def __init__(self):
        self.attribute = 'value'

def test_attr_with_existing_nested_attribute():
    obj = MockObject()
    result = _attr(obj, 'nested.attribute')
    assert result == 'value'

def test_attr_with_nonexistent_nested_attribute():
    obj = MockObject()
    result = _attr(obj, 'nested.nonexistent')
    assert result is None

def test_attr_with_partial_nonexistent_nested_attribute():
    obj = MockObject()
    result = _attr(obj, 'nonexistent.attribute')
    assert result is None

def test_attr_with_empty_attribute_string():
    obj = MockObject()
    result = _attr(obj, 'nested')
    assert result == obj.nested
