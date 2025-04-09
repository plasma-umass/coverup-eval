# file lib/ansible/plugins/action/include_vars.py:48-70
# lines [48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 67, 68, 69, 70]
# branches ['55->56', '55->60', '57->58', '57->60', '67->68', '67->69', '69->exit', '69->70']

import pytest
from unittest.mock import MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule
from ansible.module_utils.six import string_types

@pytest.fixture
def mock_task():
    return MagicMock()

@pytest.fixture
def action_module(mock_task):
    action = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    return action

def test_set_args_with_valid_extensions_string(action_module, mock_task):
    mock_task.args = {
        'extensions': 'yml'
    }
    action_module._set_args()
    assert action_module.valid_extensions == ['y', 'm', 'l']

def test_set_args_with_invalid_extensions_type(action_module, mock_task):
    mock_task.args = {
        'extensions': 123
    }
    with pytest.raises(AnsibleError, match='Invalid type for "extensions" option, it must be a list'):
        action_module._set_args()

def test_set_args_with_no_source_dir_or_file(action_module, mock_task):
    mock_task.args = {
        '_raw_params': 'some_file.yml\n'
    }
    action_module._set_args()
    assert action_module.source_file == 'some_file.yml'

def test_set_args_with_ignore_unknown_extensions(action_module, mock_task):
    mock_task.args = {
        'ignore_unknown_extensions': True
    }
    action_module._set_args()
    assert action_module.ignore_unknown_extensions is True

def test_set_args_with_files_matching(action_module, mock_task):
    mock_task.args = {
        'files_matching': '*.yml'
    }
    action_module._set_args()
    assert action_module.files_matching == '*.yml'
