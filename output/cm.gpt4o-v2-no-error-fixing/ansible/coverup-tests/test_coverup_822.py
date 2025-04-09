# file: lib/ansible/utils/helpers.py:37-43
# asked: {"lines": [42], "branches": [[41, 42]]}
# gained: {"lines": [42], "branches": [[41, 42]]}

import pytest

class TestObject:
    def __init__(self):
        self.a = 1
        self.b = 2
        self._c = 3

def test_object_to_dict_with_none_exclude():
    from ansible.utils.helpers import object_to_dict

    obj = TestObject()
    result = object_to_dict(obj, None)
    expected = {'a': 1, 'b': 2}
    assert result == expected

def test_object_to_dict_with_non_list_exclude():
    from ansible.utils.helpers import object_to_dict

    obj = TestObject()
    result = object_to_dict(obj, 'not_a_list')
    expected = {'a': 1, 'b': 2}
    assert result == expected

def test_object_to_dict_with_list_exclude():
    from ansible.utils.helpers import object_to_dict

    obj = TestObject()
    result = object_to_dict(obj, ['a'])
    expected = {'b': 2}
    assert result == expected
