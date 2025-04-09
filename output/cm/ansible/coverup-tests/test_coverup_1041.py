# file lib/ansible/module_utils/common/collections.py:43-53
# lines [43, 53]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_union():
    original_dict = ImmutableDict({'a': 1, 'b': 2})
    overriding_dict = {'b': 3, 'c': 4}

    # Perform the union operation
    new_dict = original_dict.union(overriding_dict)

    # Check that the new ImmutableDict has the correct values
    assert new_dict['a'] == 1
    assert new_dict['b'] == 3
    assert new_dict['c'] == 4

    # Check that the original ImmutableDict remains unchanged
    assert original_dict['a'] == 1
    assert original_dict['b'] == 2
    assert 'c' not in original_dict

    # Check that the result is indeed an ImmutableDict
    assert isinstance(new_dict, ImmutableDict)

    # Check that the new ImmutableDict is actually immutable
    with pytest.raises(TypeError):
        new_dict['d'] = 5
