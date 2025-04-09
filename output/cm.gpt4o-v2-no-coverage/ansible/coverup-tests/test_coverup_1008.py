# file: lib/ansible/module_utils/common/collections.py:16-17
# asked: {"lines": [16, 17], "branches": []}
# gained: {"lines": [16, 17], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_init():
    # Test with no arguments
    d = ImmutableDict()
    assert d._store == {}

    # Test with positional arguments
    d = ImmutableDict({'a': 1, 'b': 2})
    assert d._store == {'a': 1, 'b': 2}

    # Test with keyword arguments
    d = ImmutableDict(a=1, b=2)
    assert d._store == {'a': 1, 'b': 2}

    # Test with both positional and keyword arguments
    d = ImmutableDict({'a': 1}, b=2)
    assert d._store == {'a': 1, 'b': 2}
