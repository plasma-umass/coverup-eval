# file: lib/ansible/utils/helpers.py:37-43
# asked: {"lines": [37, 41, 42, 43], "branches": [[41, 42], [41, 43]]}
# gained: {"lines": [37, 41, 42, 43], "branches": [[41, 42], [41, 43]]}

import pytest
from ansible.utils.helpers import object_to_dict

class TestObject:
    def __init__(self):
        self.a = 1
        self.b = 2
        self._c = 3

def test_object_to_dict_no_exclude():
    obj = TestObject()
    result = object_to_dict(obj)
    assert result == {'a': 1, 'b': 2}

def test_object_to_dict_with_exclude():
    obj = TestObject()
    result = object_to_dict(obj, exclude=['a'])
    assert result == {'b': 2}

def test_object_to_dict_exclude_not_list():
    obj = TestObject()
    result = object_to_dict(obj, exclude='a')
    assert result == {'a': 1, 'b': 2}

def test_object_to_dict_exclude_none():
    obj = TestObject()
    result = object_to_dict(obj, exclude=None)
    assert result == {'a': 1, 'b': 2}
