# file: lib/ansible/plugins/action/include_vars.py:208-216
# asked: {"lines": [208, 215, 216], "branches": []}
# gained: {"lines": [208, 215, 216], "branches": []}

import pytest
from ansible.plugins.action.include_vars import ActionModule
from unittest.mock import patch

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_is_valid_file_ext_valid(action_module):
    action_module.valid_extensions = ['yml', 'yaml', 'json']
    assert action_module._is_valid_file_ext('test.yml') is True
    assert action_module._is_valid_file_ext('test.yaml') is True
    assert action_module._is_valid_file_ext('test.json') is True

def test_is_valid_file_ext_invalid(action_module):
    action_module.valid_extensions = ['yml', 'yaml', 'json']
    assert action_module._is_valid_file_ext('test.txt') is False
    assert action_module._is_valid_file_ext('test') is False
    assert action_module._is_valid_file_ext('test.') is False

def test_is_valid_file_ext_no_extension(action_module):
    action_module.valid_extensions = ['yml', 'yaml', 'json']
    assert action_module._is_valid_file_ext('testfile') is False

def test_is_valid_file_ext_empty_string(action_module):
    action_module.valid_extensions = ['yml', 'yaml', 'json']
    assert action_module._is_valid_file_ext('') is False
