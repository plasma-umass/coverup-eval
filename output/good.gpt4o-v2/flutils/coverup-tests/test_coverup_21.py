# file: flutils/objutils.py:36-58
# asked: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}
# gained: {"lines": [36, 55, 56, 57, 58], "branches": [[55, 56], [55, 58], [56, 55], [56, 57]]}

import pytest
from flutils.objutils import has_any_attrs

class DummyClass:
    def __init__(self):
        self.existing_attr = True

def test_has_any_attrs_with_existing_attr():
    obj = DummyClass()
    assert has_any_attrs(obj, 'existing_attr', 'non_existing_attr') is True

def test_has_any_attrs_with_non_existing_attrs():
    obj = DummyClass()
    assert has_any_attrs(obj, 'non_existing_attr1', 'non_existing_attr2') is False

def test_has_any_attrs_with_empty_attrs():
    obj = DummyClass()
    assert has_any_attrs(obj) is False

def test_has_any_attrs_with_builtin_obj():
    obj = dict()
    assert has_any_attrs(obj, 'get', 'keys', 'items', 'values', 'something') is True
    assert has_any_attrs(obj, 'something') is False
