# file: flutils/objutils.py:36-58
# asked: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}
# gained: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}

import pytest
from flutils.objutils import has_any_attrs

def test_has_any_attrs_with_existing_attributes():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'get', 'keys', 'items', 'values') is True

def test_has_any_attrs_with_non_existing_attributes():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'nonexistent', 'anothernonexistent') is False

def test_has_any_attrs_with_mixed_attributes():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'nonexistent', 'keys') is True

def test_has_any_attrs_with_no_attributes():
    obj = {'key': 'value'}
    assert has_any_attrs(obj) is False

def test_has_any_attrs_with_empty_object():
    obj = {}
    assert has_any_attrs(obj, 'get', 'keys', 'items', 'values') is True

def test_has_any_attrs_with_non_dict_object():
    class TestClass:
        def method(self):
            pass

    obj = TestClass()
    assert has_any_attrs(obj, 'method', 'nonexistent') is True
    assert has_any_attrs(obj, 'nonexistent') is False
