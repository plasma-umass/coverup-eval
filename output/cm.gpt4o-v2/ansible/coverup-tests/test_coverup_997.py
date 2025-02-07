# file: lib/ansible/module_utils/common/collections.py:16-17
# asked: {"lines": [16, 17], "branches": []}
# gained: {"lines": [16, 17], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_init_with_args():
    data = [('key1', 'value1'), ('key2', 'value2')]
    immut_dict = ImmutableDict(data)
    assert immut_dict._store == dict(data)

def test_immutable_dict_init_with_kwargs():
    data = {'key1': 'value1', 'key2': 'value2'}
    immut_dict = ImmutableDict(**data)
    assert immut_dict._store == data
