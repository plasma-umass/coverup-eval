# file: lib/ansible/module_utils/common/parameters.py:871-902
# asked: {"lines": [881, 883, 884, 886, 887, 888, 889, 890, 891, 893, 894, 895, 896, 897, 898, 900, 902], "branches": [[886, 887], [886, 902], [888, 889], [888, 893], [889, 886], [889, 890], [893, 886], [893, 894], [895, 896], [895, 897], [897, 898], [897, 900]]}
# gained: {"lines": [881, 883, 884, 886, 887, 888, 889, 890, 891, 893, 894, 895, 896, 897, 898, 902], "branches": [[886, 887], [886, 902], [888, 889], [888, 893], [889, 886], [889, 890], [893, 886], [893, 894], [895, 896], [895, 897], [897, 898]]}

import pytest
from collections import deque
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common._collections_compat import Mapping, MutableSet, MutableSequence
from ansible.module_utils.common.parameters import remove_values

def test_remove_values_with_mapping():
    value = {'key1': 'secret', 'key2': 'value2'}
    no_log_strings = ['secret']
    result = remove_values(value, no_log_strings)
    assert result == {'key1': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'key2': 'value2'}

def test_remove_values_with_mutable_sequence():
    value = ['secret', 'value2']
    no_log_strings = ['secret']
    result = remove_values(value, no_log_strings)
    assert result == ['VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'value2']

def test_remove_values_with_mutable_set():
    value = {'secret', 'value2'}
    no_log_strings = ['secret']
    result = remove_values(value, no_log_strings)
    assert result == {'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'value2'}

def test_remove_values_with_unknown_container_type():
    class CustomContainer:
        pass

    value = CustomContainer()
    no_log_strings = ['secret']
    with pytest.raises(TypeError, match='Value of unknown type'):
        remove_values(value, no_log_strings)
