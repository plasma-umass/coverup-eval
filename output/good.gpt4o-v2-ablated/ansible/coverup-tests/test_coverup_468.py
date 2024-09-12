# file: lib/ansible/module_utils/common/validation.py:530-535
# asked: {"lines": [534, 535], "branches": []}
# gained: {"lines": [534, 535], "branches": []}

import os
import pytest
from unittest.mock import patch

# Assuming check_type_str is defined somewhere in the module
from ansible.module_utils.common.validation import check_type_path

def mock_check_type_str(value):
    return str(value)

@pytest.fixture(autouse=True)
def patch_check_type_str(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.check_type_str', mock_check_type_str)

def test_check_type_path_with_string():
    input_value = '~/testpath'
    expected_value = os.path.expanduser(os.path.expandvars(input_value))
    assert check_type_path(input_value) == expected_value

def test_check_type_path_with_non_string():
    input_value = 12345
    expected_value = os.path.expanduser(os.path.expandvars(str(input_value)))
    assert check_type_path(input_value) == expected_value

def test_check_type_path_with_env_var(monkeypatch):
    monkeypatch.setenv('TEST_VAR', 'testvalue')
    input_value = '$TEST_VAR/testpath'
    expected_value = os.path.expanduser(os.path.expandvars(input_value))
    assert check_type_path(input_value) == expected_value
