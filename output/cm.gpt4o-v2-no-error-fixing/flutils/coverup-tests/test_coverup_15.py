# file: flutils/objutils.py:88-112
# asked: {"lines": [88, 109, 110, 111, 112], "branches": [[109, 110], [109, 112], [110, 109], [110, 111]]}
# gained: {"lines": [88, 109, 110, 111, 112], "branches": [[109, 110], [109, 112], [110, 109], [110, 111]]}

import pytest
from flutils.objutils import has_attrs

class DummyClass:
    def __init__(self):
        self.attr1 = 1
        self.attr2 = 2

def test_has_attrs_all_present():
    obj = DummyClass()
    assert has_attrs(obj, 'attr1', 'attr2') == True

def test_has_attrs_some_missing():
    obj = DummyClass()
    assert has_attrs(obj, 'attr1', 'attr3') == False

def test_has_attrs_none_present():
    obj = DummyClass()
    assert has_attrs(obj, 'attr3', 'attr4') == False

def test_has_attrs_empty_attrs():
    obj = DummyClass()
    assert has_attrs(obj) == True

def test_has_attrs_with_builtin():
    obj = dict()
    assert has_attrs(obj, 'get', 'keys', 'items', 'values') == True

def test_has_attrs_with_partial_builtin():
    obj = dict()
    assert has_attrs(obj, 'get', 'nonexistent') == False
