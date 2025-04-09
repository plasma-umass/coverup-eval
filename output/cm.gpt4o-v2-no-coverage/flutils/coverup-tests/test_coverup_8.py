# file: flutils/objutils.py:88-112
# asked: {"lines": [88, 109, 110, 111, 112], "branches": [[109, 110], [109, 112], [110, 109], [110, 111]]}
# gained: {"lines": [88, 109, 110, 111, 112], "branches": [[109, 110], [109, 112], [110, 109], [110, 111]]}

import pytest
from flutils.objutils import has_attrs

def test_has_attrs_all_exist():
    obj = {'a': 1, 'b': 2}
    assert has_attrs(obj, 'keys', 'items', 'get') == True

def test_has_attrs_some_missing():
    obj = {'a': 1, 'b': 2}
    assert has_attrs(obj, 'keys', 'nonexistent') == False

def test_has_attrs_none_exist():
    obj = {'a': 1, 'b': 2}
    assert has_attrs(obj, 'nonexistent1', 'nonexistent2') == False

def test_has_attrs_no_attrs():
    obj = {'a': 1, 'b': 2}
    assert has_attrs(obj) == True

def test_has_attrs_empty_obj():
    obj = {}
    assert has_attrs(obj, 'keys', 'items', 'get') == True

def test_has_attrs_non_dict_obj():
    class TestClass:
        def method1(self):
            pass
        def method2(self):
            pass

    obj = TestClass()
    assert has_attrs(obj, 'method1', 'method2') == True
    assert has_attrs(obj, 'method1', 'nonexistent') == False
