# file lib/ansible/module_utils/common/collections.py:55-65
# lines [55, 63, 64, 65]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_difference():
    original_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    subtractive_iterable = ['b', 'c']
    expected_dict = ImmutableDict({'a': 1})

    result_dict = original_dict.difference(subtractive_iterable)

    assert isinstance(result_dict, ImmutableDict), "Result should be an ImmutableDict"
    assert result_dict == expected_dict, "Resulting ImmutableDict does not match expected"
    assert 'b' not in result_dict, "'b' should have been removed from the ImmutableDict"
    assert 'c' not in result_dict, "'c' should have been removed from the ImmutableDict"
