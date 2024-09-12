# file: flutils/objutils.py:36-58
# asked: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}
# gained: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}

import pytest
from flutils.objutils import has_any_attrs

def test_has_any_attrs_with_existing_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'get', 'keys', 'items', 'values', 'something') is True

def test_has_any_attrs_with_no_existing_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'nonexistent_attr1', 'nonexistent_attr2') is False

def test_has_any_attrs_with_empty_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj) is False

def test_has_any_attrs_with_non_dict_object():
    class TestClass:
        def method(self):
            pass

    obj = TestClass()
    assert has_any_attrs(obj, 'method', 'nonexistent_method') is True
    assert has_any_attrs(obj, 'nonexistent_method') is False

def test_has_any_attrs_with_mixed_attrs():
    obj = {'key': 'value'}
    assert has_any_attrs(obj, 'nonexistent_attr', 'keys') is True
    assert has_any_attrs(obj, 'nonexistent_attr', 'nonexistent_attr2') is False
