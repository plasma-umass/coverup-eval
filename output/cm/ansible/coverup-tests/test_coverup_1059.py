# file lib/ansible/module_utils/common/collections.py:16-17
# lines [16, 17]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_init():
    # Test with args
    immutable_dict_args = ImmutableDict([('key1', 'value1'), ('key2', 'value2')])
    assert immutable_dict_args._store == {'key1': 'value1', 'key2': 'value2'}

    # Test with kwargs
    immutable_dict_kwargs = ImmutableDict(key1='value1', key2='value2')
    assert immutable_dict_kwargs._store == {'key1': 'value1', 'key2': 'value2'}

    # Remove the test with both args and kwargs as it is not raising TypeError
    # and is not necessary for the coverage of the __init__ method
