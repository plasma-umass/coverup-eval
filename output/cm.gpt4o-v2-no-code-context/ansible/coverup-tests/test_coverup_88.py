# file: lib/ansible/plugins/action/include_vars.py:27-46
# asked: {"lines": [27, 28, 29, 31, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45], "branches": [[28, 29], [28, 31], [31, 32], [31, 34], [36, 37], [36, 39], [39, 40], [39, 42], [42, 0], [42, 43]]}
# gained: {"lines": [27, 28, 29, 31, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45], "branches": [[28, 29], [31, 32], [31, 34], [36, 37], [36, 39], [39, 40], [39, 42], [42, 0], [42, 43]]}

import pytest
import re
from ansible.plugins.action.include_vars import ActionModule
from ansible.errors import AnsibleError

@pytest.fixture
def action_module():
    class MockActionModule(ActionModule):
        def __init__(self):
            self.depth = None
            self.files_matching = None
            self.ignore_files = None
            self.matcher = None

    return MockActionModule()

def test_set_dir_defaults_depth(action_module):
    action_module.depth = None
    action_module._set_dir_defaults()
    assert action_module.depth == 0

def test_set_dir_defaults_files_matching(action_module):
    action_module.files_matching = '.*\.yml'
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
