# file: lib/ansible/plugins/action/reboot.py:137-156
# asked: {"lines": [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156], "branches": [[146, 147], [146, 150]]}
# gained: {"lines": [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156], "branches": [[146, 147], [146, 150]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def mock_task():
    return MagicMock()

@pytest.fixture
def mock_task_vars():
    return {
        'ansible_facts': {
            'ansible_distribution': 'Ubuntu',
            'ansible_distribution_version': '20.04',
            'ansible_os_family': 'Debian'
        }
    }

@pytest.fixture
def action_module(mock_task):
    return ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_get_distribution_success(action_module, mock_task_vars):
    with patch.object(action_module, '_execute_module', return_value={
        'ansible_facts': mock_task_vars['ansible_facts'],
        'failed': False
    }):
        distribution = action_module.get_distribution(mock_task_vars)
        assert distribution['name'] == 'ubuntu'
        assert distribution['version'] == '20'
        assert distribution['family'] == 'debian'

def test_get_distribution_failure(action_module, mock_task_vars):
    with patch.object(action_module, '_execute_module', return_value={
        'module_stdout': 'Some error',
        'module_stderr': 'Some stderr',
        'failed': True
    }):
        with pytest.raises(AnsibleError, match='Failed to determine system distribution'):
            action_module.get_distribution(mock_task_vars)

def test_get_distribution_key_error(action_module, mock_task_vars):
    with patch.object(action_module, '_execute_module', return_value={
        'ansible_facts': {},
        'failed': False
    }):
        with pytest.raises(AnsibleError, match='Failed to get distribution information. Missing'):
            action_module.get_distribution(mock_task_vars)
