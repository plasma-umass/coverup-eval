# file: lib/ansible/plugins/action/reboot.py:137-156
# asked: {"lines": [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156], "branches": [[146, 147], [146, 150]]}
# gained: {"lines": [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156], "branches": [[146, 147], [146, 150]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils._text import to_native, to_text
from unittest.mock import patch, MagicMock

@pytest.fixture
def action_module(mocker):
    task = MagicMock()
    task.action = 'reboot'
    return ActionModule(task=task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_get_distribution_success(action_module, mocker):
    task_vars = {}
    module_output = {
        'ansible_facts': {
            'ansible_distribution': 'Ubuntu',
            'ansible_distribution_version': '20.04',
            'ansible_os_family': 'Debian'
        }
    }
    mocker.patch.object(action_module, '_execute_module', return_value=module_output)
    distribution = action_module.get_distribution(task_vars)
    assert distribution['name'] == 'ubuntu'
    assert distribution['version'] == '20'
    assert distribution['family'] == 'debian'

def test_get_distribution_failed(action_module, mocker):
    task_vars = {}
    module_output = {
        'failed': True,
        'module_stdout': 'Some error',
        'module_stderr': 'Some stderr'
    }
    mocker.patch.object(action_module, '_execute_module', return_value=module_output)
    with pytest.raises(AnsibleError, match='Failed to determine system distribution'):
        action_module.get_distribution(task_vars)

def test_get_distribution_key_error(action_module, mocker):
    task_vars = {}
    module_output = {
        'ansible_facts': {
            'ansible_distribution': 'Ubuntu',
            'ansible_distribution_version': '20.04'
            # Missing 'ansible_os_family'
        }
    }
    mocker.patch.object(action_module, '_execute_module', return_value=module_output)
    with pytest.raises(AnsibleError, match='Failed to get distribution information. Missing "ansible_os_family" in output.'):
        action_module.get_distribution(task_vars)
