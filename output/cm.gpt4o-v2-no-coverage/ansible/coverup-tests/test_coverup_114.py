# file: lib/ansible/module_utils/common/parameters.py:871-902
# asked: {"lines": [871, 881, 883, 884, 886, 887, 888, 889, 890, 891, 893, 894, 895, 896, 897, 898, 900, 902], "branches": [[886, 887], [886, 902], [888, 889], [888, 893], [889, 886], [889, 890], [893, 886], [893, 894], [895, 896], [895, 897], [897, 898], [897, 900]]}
# gained: {"lines": [871, 881, 883, 884, 886, 902], "branches": [[886, 902]]}

import pytest
from collections import deque
from unittest.mock import patch
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common._collections_compat import Mapping, MutableSet, MutableSequence
from ansible.module_utils.common.parameters import remove_values

# Mock _remove_values_conditions
def mock_remove_values_conditions(value, no_log_strings, deferred_removals):
    if isinstance(value, str) and value in no_log_strings:
        return 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'
    if isinstance(value, list):
        return ['VALUE_SPECIFIED_IN_NO_LOG_PARAMETER' if v in no_log_strings else v for v in value]
    if isinstance(value, dict):
        return {k: 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER' if v in no_log_strings else v for k, v in value.items()}
    if isinstance(value, set):
        return {'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER' if v in no_log_strings else v for v in value}
    return value

@pytest.fixture
def mock_remove_conditions(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.parameters._remove_values_conditions', mock_remove_values_conditions)

def test_remove_values_with_string(mock_remove_conditions):
    value = "sensitive_data"
    no_log_strings = ["sensitive_data"]
    result = remove_values(value, no_log_strings)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_remove_values_with_list(mock_remove_conditions):
    value = ["sensitive_data", "public_data"]
    no_log_strings = ["sensitive_data"]
    result = remove_values(value, no_log_strings)
    assert result == ["VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "public_data"]

def test_remove_values_with_dict(mock_remove_conditions):
    value = {"key1": "sensitive_data", "key2": "public_data"}
    no_log_strings = ["sensitive_data"]
    result = remove_values(value, no_log_strings)
    assert result == {"key1": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "key2": "public_data"}

def test_remove_values_with_set(mock_remove_conditions):
    value = {"sensitive_data", "public_data"}
    no_log_strings = ["sensitive_data"]
    result = remove_values(value, no_log_strings)
    assert result == {"VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "public_data"}

def test_remove_values_with_unknown_container_type():
    class CustomContainer:
        pass

    value = CustomContainer()
    no_log_strings = ["sensitive_data"]
    with pytest.raises(TypeError, match='Value of unknown type'):
        remove_values(value, no_log_strings)
