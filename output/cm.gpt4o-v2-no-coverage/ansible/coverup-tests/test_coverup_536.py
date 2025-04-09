# file: lib/ansible/module_utils/common/collections.py:31-38
# asked: {"lines": [31, 32, 33, 34, 35, 36, 38], "branches": [[33, 34], [33, 38]]}
# gained: {"lines": [31, 32, 33, 34, 35, 36, 38], "branches": [[33, 34], [33, 38]]}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_eq():
    dict1 = ImmutableDict(a=1, b=2)
    dict2 = ImmutableDict(a=1, b=2)
    dict3 = ImmutableDict(a=1, b=3)
    non_dict = {'a': 1, 'b': 2}

    # Test equality with same content
    assert dict1 == dict2

    # Test inequality with different content
    assert dict1 != dict3

    # Test equality with a non-ImmutableDict object
    assert dict1 != non_dict

    # Test TypeError handling in __eq__
    class Unhashable:
        def __hash__(self):
            raise TypeError("unhashable type")

    unhashable = Unhashable()
    assert dict1 != unhashable
