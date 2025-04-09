# file lib/ansible/module_utils/common/parameters.py:827-868
# lines [827, 841, 843, 844, 846, 847, 849, 850, 851, 852, 856, 857, 859, 860, 861, 862, 863, 864, 866, 868]
# branches ['846->847', '846->868', '849->850', '849->859', '850->846', '850->851', '851->852', '851->856', '859->846', '859->860', '861->862', '861->863', '863->864', '863->866']

import pytest
from collections import deque
from collections.abc import Mapping, MutableSequence, MutableSet
from ansible.module_utils.common.parameters import sanitize_keys

# Mocking the required functions
def to_native(value, errors='strict'):
    return str(value)

def _sanitize_keys_conditions(obj, no_log_strings, ignore_keys, deferred_removals):
    if isinstance(obj, (Mapping, MutableSequence, MutableSet)):
        return obj
    raise TypeError('Unknown container type encountered when removing private values from keys')

def _remove_values_conditions(key, no_log_strings, deferred_removals):
    return key

# Injecting the mocks into the module under test
@pytest.fixture(autouse=True)
def mock_functions(mocker):
    mocker.patch('ansible.module_utils.common.parameters.to_native', side_effect=to_native)
    mocker.patch('ansible.module_utils.common.parameters._sanitize_keys_conditions', side_effect=_sanitize_keys_conditions)
    mocker.patch('ansible.module_utils.common.parameters._remove_values_conditions', side_effect=_remove_values_conditions)

# Test function to cover the missing branches
def test_sanitize_keys_with_unknown_container_type():
    with pytest.raises(TypeError):
        sanitize_keys(obj=object(), no_log_strings=set(), ignore_keys=frozenset())

# Test function to cover the branch with a Mapping
def test_sanitize_keys_with_mapping():
    test_dict = {'key1': 'value1', '_ansible_key2': 'value2'}
    sanitized = sanitize_keys(obj=test_dict, no_log_strings={'value1'}, ignore_keys=frozenset({'key1'}))
    assert '_ansible_key2' in sanitized
    assert 'key1' in sanitized

# Test function to cover the branch with a MutableSequence
def test_sanitize_keys_with_mutable_sequence():
    test_list = ['value1', 'value2']
    sanitized = sanitize_keys(obj=test_list, no_log_strings={'value1'}, ignore_keys=frozenset())
    assert 'value1' in sanitized
    assert 'value2' in sanitized

# Test function to cover the branch with a MutableSet
def test_sanitize_keys_with_mutable_set():
    test_set = {'value1', 'value2'}
    sanitized = sanitize_keys(obj=test_set, no_log_strings={'value1'}, ignore_keys=frozenset())
    assert 'value1' in sanitized
    assert 'value2' in sanitized
