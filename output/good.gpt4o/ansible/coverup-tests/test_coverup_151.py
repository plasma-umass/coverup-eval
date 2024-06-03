# file lib/ansible/plugins/action/include_vars.py:27-46
# lines [27, 28, 29, 31, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45]
# branches ['28->29', '28->31', '31->32', '31->34', '36->37', '36->39', '39->40', '39->42', '42->exit', '42->43']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.include_vars import ActionModule
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def action_module():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = DataLoader()
    templar = Templar(loader=loader)
    shared_loader_obj = MagicMock()
    action = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    action.depth = None
    action.files_matching = None
    action.ignore_files = None
    return action

def test_set_dir_defaults_depth(action_module):
    action_module.depth = None
    action_module._set_dir_defaults()
    assert action_module.depth == 0

def test_set_dir_defaults_files_matching(action_module):
    action_module.files_matching = '.*\.yml$'
    action_module._set_dir_defaults()
    assert action_module.matcher is not None
    assert action_module.matcher.match('test.yml')

def test_set_dir_defaults_no_files_matching(action_module):
    action_module.files_matching = None
    action_module._set_dir_defaults()
    assert action_module.matcher is None

def test_set_dir_defaults_ignore_files_none(action_module):
    action_module.ignore_files = None
    action_module._set_dir_defaults()
    assert action_module.ignore_files == []

def test_set_dir_defaults_ignore_files_string(action_module):
    action_module.ignore_files = 'file1 file2'
    action_module._set_dir_defaults()
    assert action_module.ignore_files == ['file1', 'file2']

def test_set_dir_defaults_ignore_files_dict(action_module):
    action_module.ignore_files = {'key': 'value'}
    result = action_module._set_dir_defaults()
    assert result == {
        'failed': True,
        'message': "{'key': 'value'} must be a list"
    }
