# file: lib/ansible/module_utils/common/parameters.py:871-902
# asked: {"lines": [887, 888, 889, 890, 891, 893, 894, 895, 896, 897, 898, 900], "branches": [[886, 887], [888, 889], [888, 893], [889, 886], [889, 890], [893, 886], [893, 894], [895, 896], [895, 897], [897, 898], [897, 900]]}
# gained: {"lines": [887, 888, 889, 890, 891, 893, 894, 895, 896, 897, 898], "branches": [[886, 887], [888, 889], [888, 893], [889, 886], [889, 890], [893, 886], [893, 894], [895, 896], [895, 897], [897, 898]]}

import pytest
from collections import deque
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common._collections_compat import Mapping, MutableSet, MutableSequence
from ansible.module_utils.common.parameters import remove_values

def test_remove_values_scalar():
    value = "sensitive_data"
    no_log_strings = ["sensitive"]
    result = remove_values(value, no_log_strings)
    assert result == "********_data"

def test_remove_values_list():
    value = ["sensitive_data", "public_data"]
    no_log_strings = ["sensitive"]
    result = remove_values(value, no_log_strings)
    assert result == ["********_data", "public_data"]

def test_remove_values_dict():
    value = {"key1": "sensitive_data", "key2": "public_data"}
    no_log_strings = ["sensitive"]
    result = remove_values(value, no_log_strings)
    assert result == {"key1": "********_data", "key2": "public_data"}

def test_remove_values_nested():
    value = {"key1": ["sensitive_data", {"key2": "public_data"}]}
    no_log_strings = ["sensitive"]
    result = remove_values(value, no_log_strings)
    assert result == {"key1": ["********_data", {"key2": "public_data"}]}

def test_remove_values_set():
    value = {"sensitive_data", "public_data"}
    no_log_strings = ["sensitive"]
    result = remove_values(value, no_log_strings)
    assert result == {"********_data", "public_data"}

def test_remove_values_integer():
    value = 12345
    no_log_strings = ["123"]
    result = remove_values(value, no_log_strings)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
