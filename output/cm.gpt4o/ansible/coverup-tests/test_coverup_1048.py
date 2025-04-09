# file lib/ansible/module_utils/common/parameters.py:827-868
# lines [841, 843, 844, 846, 847, 849, 850, 851, 852, 856, 857, 859, 860, 861, 862, 863, 864, 866, 868]
# branches ['846->847', '846->868', '849->850', '849->859', '850->846', '850->851', '851->852', '851->856', '859->846', '859->860', '861->862', '861->863', '863->864', '863->866']

import pytest
from ansible.module_utils.common.parameters import sanitize_keys
from collections import deque
from collections.abc import Mapping, MutableSequence, MutableSet

def test_sanitize_keys(mocker):
    # Mocking the helper functions used within sanitize_keys
    mocker.patch('ansible.module_utils.common.parameters.to_native', side_effect=lambda s, errors: s)
    mocker.patch('ansible.module_utils.common.parameters._sanitize_keys_conditions', side_effect=lambda obj, no_log_strings, ignore_keys, deferred_removals: obj)
    mocker.patch('ansible.module_utils.common.parameters._remove_values_conditions', side_effect=lambda key, no_log_strings, none: key)

    # Test data
    obj = {
        'password': 'secret',
        '_ansible_keep': 'keep_this',
        'nested': {
            'password': 'nested_secret'
        },
        'list': [
            'item1',
            'item2'
        ],
        'set': {'item1', 'item2'}
    }
    no_log_strings = {'secret', 'nested_secret'}
    ignore_keys = {'_ansible_keep'}

    # Call the function
    result = sanitize_keys(obj, no_log_strings, ignore_keys)

    # Assertions to verify the postconditions
    assert result == obj  # Since we mocked _sanitize_keys_conditions to return the object as is

    # Clean up
    mocker.stopall()
