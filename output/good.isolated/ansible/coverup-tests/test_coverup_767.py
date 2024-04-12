# file lib/ansible/plugins/action/include_vars.py:208-216
# lines [208, 215, 216]
# branches []

import os
import pytest
from ansible.plugins.action.include_vars import ActionModule
from unittest.mock import MagicMock

# Define a fixture for the ActionModule with mocked valid_extensions
@pytest.fixture
def action_module():
    action_module = ActionModule(None, None, None, None, None, None)
    action_module.valid_extensions = ['yml', 'yaml', 'json']
    return action_module

# Test function to check valid file extensions
def test_is_valid_file_ext_with_valid_extensions(action_module):
    assert action_module._is_valid_file_ext('/path/to/valid_file.yml') is True
    assert action_module._is_valid_file_ext('/path/to/valid_file.yaml') is True
    assert action_module._is_valid_file_ext('/path/to/valid_file.json') is True

# Test function to check invalid file extensions
def test_is_valid_file_ext_with_invalid_extensions(action_module):
    assert action_module._is_valid_file_ext('/path/to/invalid_file.txt') is False
    assert action_module._is_valid_file_ext('/path/to/invalid_file.py') is False
    assert action_module._is_valid_file_ext('/path/to/invalid_file.ini') is False

# Test function to check file without extension
def test_is_valid_file_ext_without_extension(action_module):
    assert action_module._is_valid_file_ext('/path/to/no_extension') is False

# Test function to check file with only extension and no basename
def test_is_valid_file_ext_with_only_extension(action_module):
    assert action_module._is_valid_file_ext('.yml') is False
