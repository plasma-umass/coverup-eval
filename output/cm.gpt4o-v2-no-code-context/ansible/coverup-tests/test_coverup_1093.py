# file: lib/ansible/plugins/action/include_vars.py:27-46
# asked: {"lines": [], "branches": [[28, 31]]}
# gained: {"lines": [], "branches": [[28, 31]]}

import pytest
import re
from ansible.plugins.action.include_vars import ActionModule
from ansible.errors import AnsibleError

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_set_dir_defaults_no_depth(action_module):
    action_module.depth = None
    action_module.files_matching = None
    action_module.ignore_files = None
    action_module._set_dir_defaults()
    assert action_module.depth == 0

def test_set_dir_defaults_with_files_matching(action_module):
    action_module.depth = 1
    action_module.files_matching = '.*\.yml'
    action_module.ignore_files = None
    action_module._set_dir_defaults()
    assert action_module.matcher is not None
    assert action_module.matcher.pattern == '.*\\.yml'

def test_set_dir_defaults_no_files_matching(action_module):
    action_module.depth = 1
    action_module.files_matching = None
    action_module.ignore_files = None
    action_module._set_dir_defaults()
    assert action_module.matcher is None

def test_set_dir_defaults_no_ignore_files(action_module):
    action_module.depth = 1
    action_module.files_matching = None
    action_module.ignore_files = None
    action_module._set_dir_defaults()
    assert action_module.ignore_files == []

def test_set_dir_defaults_ignore_files_string(action_module):
    action_module.depth = 1
    action_module.files_matching = None
    action_module.ignore_files = 'file1 file2'
    action_module._set_dir_defaults()
    assert action_module.ignore_files == ['file1', 'file2']

def test_set_dir_defaults_ignore_files_dict(action_module):
    action_module.depth = 1
    action_module.files_matching = None
    action_module.ignore_files = {'key': 'value'}
    result = action_module._set_dir_defaults()
    assert result == {
        'failed': True,
        'message': "{'key': 'value'} must be a list"
    }
