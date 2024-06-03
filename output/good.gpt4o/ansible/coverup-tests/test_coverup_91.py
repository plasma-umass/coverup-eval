# file lib/ansible/module_utils/common/parameters.py:871-902
# lines [871, 881, 883, 884, 886, 887, 888, 889, 890, 891, 893, 894, 895, 896, 897, 898, 900, 902]
# branches ['886->887', '886->902', '888->889', '888->893', '889->886', '889->890', '893->886', '893->894', '895->896', '895->897', '897->898', '897->900']

import pytest
from collections import deque
from collections.abc import Mapping, MutableSequence, MutableSet
from ansible.module_utils.common.parameters import remove_values

def _remove_values_conditions(value, no_log_strings, deferred_removals):
    if isinstance(value, str):
        for no_log_string in no_log_strings:
            if no_log_string in value:
                return value.replace(no_log_string, '********')
        return value
    elif isinstance(value, Mapping):
        new_value = {}
        deferred_removals.append((value, new_value))
        return new_value
    elif isinstance(value, MutableSequence):
        new_value = []
        deferred_removals.append((value, new_value))
        return new_value
    elif isinstance(value, MutableSet):
        new_value = set()
        deferred_removals.append((value, new_value))
        return new_value
    else:
        return value

@pytest.fixture
def mock_remove_values_conditions(mocker):
    return mocker.patch('ansible.module_utils.common.parameters._remove_values_conditions', side_effect=_remove_values_conditions)

def test_remove_values(mock_remove_values_conditions):
    no_log_strings = ['secret', 'password']
    value = {
        'key1': 'value1',
        'key2': 'secret_value',
        'key3': ['password123', 'value3'],
        'key4': {'nested_key': 'nested_secret_value'},
        'key5': {'set_key': {'password_set'}}
    }

    expected_value = {
        'key1': 'value1',
        'key2': '********_value',
        'key3': ['********123', 'value3'],
        'key4': {'nested_key': 'nested_********_value'},
        'key5': {'set_key': {'********_set'}}
    }

    result = remove_values(value, no_log_strings)
    assert result == expected_value

    # Ensure that the deferred removals were processed correctly
    assert mock_remove_values_conditions.call_count > 1
