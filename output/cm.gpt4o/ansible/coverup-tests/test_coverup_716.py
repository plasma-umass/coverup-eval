# file lib/ansible/plugins/action/include_vars.py:208-216
# lines [208, 215, 216]
# branches []

import pytest
from unittest.mock import Mock
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    task = Mock()
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    module.valid_extensions = ['yml', 'yaml', 'json']
    return module

def test_is_valid_file_ext_valid(action_module):
    assert action_module._is_valid_file_ext('test.yml') is True
    assert action_module._is_valid_file_ext('test.yaml') is True
    assert action_module._is_valid_file_ext('test.json') is True

def test_is_valid_file_ext_invalid(action_module):
    assert action_module._is_valid_file_ext('test.txt') is False
    assert action_module._is_valid_file_ext('test') is False
    assert action_module._is_valid_file_ext('test.') is False

def test_is_valid_file_ext_no_extension(action_module):
    assert action_module._is_valid_file_ext('testfile') is False

def test_is_valid_file_ext_empty_string(action_module):
    assert action_module._is_valid_file_ext('') is False
