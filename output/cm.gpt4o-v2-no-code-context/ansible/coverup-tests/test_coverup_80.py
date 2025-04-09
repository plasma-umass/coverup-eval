# file: lib/ansible/plugins/action/include_vars.py:48-70
# asked: {"lines": [48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 67, 68, 69, 70], "branches": [[55, 56], [55, 60], [57, 58], [57, 60], [67, 68], [67, 69], [69, 0], [69, 70]]}
# gained: {"lines": [48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 67, 68, 69, 70], "branches": [[55, 56], [55, 60], [57, 58], [57, 60], [67, 68], [67, 69], [69, 0], [69, 70]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule
from ansible.playbook.task import Task
from ansible.utils.vars import load_extra_vars

@pytest.fixture
def action_module():
    task = Task()
    task.args = {}
    return ActionModule(task=task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_set_args_no_source(action_module):
    action_module._task.args = {
        'hash_behaviour': 'merge',
        'name': 'test_name',
        'depth': 2,
        'files_matching': '*.yml',
        'ignore_unknown_extensions': True,
        'ignore_files': ['ignore_this.yml'],
        'extensions': 'yml'
    }
    action_module._set_args()
    assert action_module.hash_behaviour == 'merge'
    assert action_module.return_results_as_name == 'test_name'
    assert action_module.source_dir is None
    assert action_module.source_file is None
    assert action_module.depth == 2
    assert action_module.files_matching == '*.yml'
    assert action_module.ignore_unknown_extensions is True
    assert action_module.ignore_files == ['ignore_this.yml']
    assert action_module.valid_extensions == ['y', 'm', 'l']

def test_set_args_with_source_file(action_module):
    action_module._task.args = {
        'file': 'test_file.yml'
    }
    action_module._set_args()
    assert action_module.source_file == 'test_file.yml'

def test_set_args_with_raw_params(action_module):
    action_module._task.args = {
        '_raw_params': 'test_raw_file.yml\n'
    }
    action_module._set_args()
    assert action_module.source_file == 'test_raw_file.yml'

def test_set_args_invalid_extensions(action_module):
    action_module._task.args = {
        'extensions': 123
    }
    with pytest.raises(AnsibleError, match='Invalid type for "extensions" option, it must be a list'):
        action_module._set_args()

def test_set_args_valid_extensions_list(action_module):
    action_module._task.args = {
        'extensions': ['yml', 'yaml']
    }
    action_module._set_args()
    assert action_module.valid_extensions == ['yml', 'yaml']
