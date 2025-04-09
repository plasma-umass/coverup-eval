# file: lib/ansible/utils/helpers.py:37-43
# asked: {"lines": [37, 41, 42, 43], "branches": [[41, 42], [41, 43]]}
# gained: {"lines": [37, 41, 42, 43], "branches": [[41, 42], [41, 43]]}

import pytest

class DummyObject:
    def __init__(self, a, b, _c):
        self.a = a
        self.b = b
        self._c = _c

def test_object_to_dict_no_exclude():
    from ansible.utils.helpers import object_to_dict

    obj = DummyObject(a=1, b=2, _c=3)
    result = object_to_dict(obj)
    assert result == {'a': 1, 'b': 2}

def test_object_to_dict_with_exclude():
    from ansible.utils.helpers import object_to_dict

    obj = DummyObject(a=1, b=2, _c=3)
    result = object_to_dict(obj, exclude=['b'])
    assert result == {'a': 1}

def test_object_to_dict_exclude_not_list():
    from ansible.utils.helpers import object_to_dict

    obj = DummyObject(a=1, b=2, _c=3)
    result = object_to_dict(obj, exclude='b')
    assert result == {'a': 1, 'b': 2}
