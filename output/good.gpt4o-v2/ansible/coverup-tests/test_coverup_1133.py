# file: lib/ansible/plugins/action/include_vars.py:48-70
# asked: {"lines": [51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 67, 68, 69, 70], "branches": [[55, 56], [55, 60], [57, 58], [57, 60], [67, 68], [67, 69], [69, 0], [69, 70]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 67, 68, 69, 70], "branches": [[55, 56], [55, 60], [57, 58], [57, 60], [67, 68], [67, 69], [69, 0], [69, 70]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.six import string_types
from ansible.plugins.action.include_vars import ActionModule
from unittest.mock import Mock

class MockTask:
    def __init__(self, args):
        self.args = args

@pytest.fixture
def action_module():
    task = MockTask({})
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_set_args_no_source(action_module):
    action_module._task.args = {}
    action_module._set_args()
    assert action_module.source_file is None

def test_set_args_with_source_file(action_module):
    action_module._task.args = {'file': 'test_file'}
    action_module._set_args()
    assert action_module.source_file == 'test_file'

def test_set_args_with_raw_params(action_module):
    action_module._task.args = {'_raw_params': 'test_file\n'}
    action_module._set_args()
    assert action_module.source_file == 'test_file'

def test_set_args_with_valid_extensions_string(action_module):
    action_module._task.args = {'extensions': 'yml'}
    action_module._set_args()
    assert action_module.valid_extensions == ['y', 'm', 'l']

def test_set_args_with_invalid_extensions_type(action_module):
    action_module._task.args = {'extensions': 123}
    with pytest.raises(AnsibleError, match='Invalid type for "extensions" option, it must be a list'):
        action_module._set_args()
