# file flutils/objutils.py:88-112
# lines [88, 109, 110, 111, 112]
# branches ['109->110', '109->112', '110->109', '110->111']

import pytest
from flutils.objutils import has_attrs

class DummyClass:
    def __init__(self):
        self.attr1 = "value1"
        self.attr2 = "value2"

def test_has_attrs_with_all_attrs():
    obj = DummyClass()
    assert has_attrs(obj, 'attr1', 'attr2') is True

def test_has_attrs_with_missing_attr():
    obj = DummyClass()
    assert has_attrs(obj, 'attr1', 'attr3') is False

def test_has_attrs_with_no_attrs():
    obj = DummyClass()
    assert has_attrs(obj) is True

def test_has_attrs_with_non_existent_attrs():
    obj = DummyClass()
    assert has_attrs(obj, 'non_existent_attr') is False

def test_has_attrs_with_builtin_object():
    obj = dict()
    assert has_attrs(obj, 'get', 'keys', 'items', 'values') is True
