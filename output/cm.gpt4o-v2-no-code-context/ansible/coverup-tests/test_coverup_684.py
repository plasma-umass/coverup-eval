# file: lib/ansible/module_utils/common/validation.py:530-535
# asked: {"lines": [530, 534, 535], "branches": []}
# gained: {"lines": [530, 534, 535], "branches": []}

import pytest
import os
from ansible.module_utils.common.validation import check_type_path

def test_check_type_path_string(monkeypatch):
    # Mock check_type_str to return the same value
    def mock_check_type_str(value):
        return value

    monkeypatch.setattr('ansible.module_utils.common.validation.check_type_str', mock_check_type_str)

    # Test with a simple string
    input_value = '~/test_path'
    expected_value = os.path.expanduser(os.path.expandvars(input_value))
    assert check_type_path(input_value) == expected_value

def test_check_type_path_non_string(monkeypatch):
    # Mock check_type_str to convert non-string to string
    def mock_check_type_str(value):
        return str(value)

    monkeypatch.setattr('ansible.module_utils.common.validation.check_type_str', mock_check_type_str)

    # Test with a non-string value
    input_value = 12345
    expected_value = os.path.expanduser(os.path.expandvars(str(input_value)))
    assert check_type_path(input_value) == expected_value
