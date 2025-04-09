# file lib/ansible/module_utils/common/parameters.py:871-902
# lines [881, 883, 884, 886, 887, 888, 889, 890, 891, 893, 894, 895, 896, 897, 898, 900, 902]
# branches ['886->887', '886->902', '888->889', '888->893', '889->886', '889->890', '893->886', '893->894', '895->896', '895->897', '897->898', '897->900']

import pytest
from collections import deque
from collections.abc import Mapping, MutableSequence, MutableSet
from ansible.module_utils.common.parameters import remove_values
from ansible.module_utils._text import to_native

def test_remove_values_with_nested_containers(mocker):
    # Mock the _remove_values_conditions to control the behavior of the function
    mocker.patch('ansible.module_utils.common.parameters._remove_values_conditions', side_effect=lambda x, y, z: x)

    # Create a nested container with a mix of Mapping, MutableSequence, and MutableSet
    nested_container = {
        'key1': ['value1', 'value2', {'inner_key': 'inner_value'}],
        'key2': {'nested_key': 'nested_value'},
        'key3': set(['value3', 'value4'])
    }

    # Define no_log_strings to be removed
    no_log_strings = ['value1', 'value2', 'inner_value', 'nested_value', 'value3', 'value4']

    # Call the remove_values function with the nested container
    result = remove_values(nested_container, no_log_strings)

    # Assertions to ensure the postconditions are met
    # Since the mock does not actually remove the values, we should assert that the values are still there
    assert 'value1' in result['key1']
    assert 'value2' in result['key1']
    assert 'inner_value' in result['key1'][2]['inner_key']
    assert 'nested_value' in result['key2']['nested_key']
    assert 'value3' in result['key3']
    assert 'value4' in result['key3']

    # Clean up the mocker
    mocker.stopall()
