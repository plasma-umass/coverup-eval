# file: lib/ansible/module_utils/common/validation.py:530-535
# asked: {"lines": [530, 534, 535], "branches": []}
# gained: {"lines": [530, 534, 535], "branches": []}

import pytest
import os
from ansible.module_utils.common.validation import check_type_path

def test_check_type_path_with_string():
    # Test with a string path
    path = "~/test_path"
    expanded_path = os.path.expanduser(os.path.expandvars(path))
    assert check_type_path(path) == expanded_path

def test_check_type_path_with_non_string():
    # Test with a non-string path
    path = 12345
    expanded_path = os.path.expanduser(os.path.expandvars(str(path)))
    assert check_type_path(path) == expanded_path

def test_check_type_path_with_env_variable(monkeypatch):
    # Test with a path containing an environment variable
    monkeypatch.setenv('TEST_VAR', 'test_value')
    path = "$TEST_VAR/test_path"
    expanded_path = os.path.expanduser(os.path.expandvars(path))
    assert check_type_path(path) == expanded_path
