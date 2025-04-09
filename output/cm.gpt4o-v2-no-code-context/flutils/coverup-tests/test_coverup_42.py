# file: flutils/objutils.py:206-231
# asked: {"lines": [206, 228, 229, 230, 231], "branches": [[228, 229], [228, 231], [229, 228], [229, 230]]}
# gained: {"lines": [206, 228, 229, 230, 231], "branches": [[228, 229], [228, 231], [229, 228], [229, 230]]}

import pytest
from collections.abc import ValuesView, KeysView
from collections import UserList
from flutils.objutils import is_subclass_of_any

def test_is_subclass_of_any_true():
    obj = dict(a=1, b=2)
    assert is_subclass_of_any(obj.keys(), ValuesView, KeysView, UserList) == True

def test_is_subclass_of_any_false():
    obj = dict(a=1, b=2)
    assert is_subclass_of_any(obj.keys(), UserList) == False

def test_is_subclass_of_any_no_classes():
    obj = dict(a=1, b=2)
    assert is_subclass_of_any(obj.keys()) == False

def test_is_subclass_of_any_non_iterable():
    obj = 42
    assert is_subclass_of_any(obj, int, float) == True

def test_is_subclass_of_any_multiple_classes():
    class CustomClass:
        pass

    class AnotherClass(CustomClass):
        pass

    obj = AnotherClass()
    assert is_subclass_of_any(obj, CustomClass, int, float) == True
