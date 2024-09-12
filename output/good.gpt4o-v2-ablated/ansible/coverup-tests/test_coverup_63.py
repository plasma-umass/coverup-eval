# file: lib/ansible/plugins/action/reboot.py:137-156
# asked: {"lines": [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156], "branches": [[146, 147], [146, 150]]}
# gained: {"lines": [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156], "branches": [[146, 147], [146, 150]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display

@pytest.fixture
def action_module():
    return ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())

@pytest.fixture
def task_vars():
    return {'ansible_facts': {}}

def test_get_distribution_success(monkeypatch, action_module, task_vars):
    display = MagicMock()
    monkeypatch.setattr('ansible.plugins.action.reboot.display', display)
    
    module_output = {
        'ansible_facts': {
            'ansible_distribution': 'Ubuntu',
            'ansible_distribution_version': '20.04',
            'ansible_os_family': 'Debian'
        }
    }
    
    action_module._execute_module = MagicMock(return_value=module_output)
    
    result = action_module.get_distribution(task_vars)
    
    assert result == {
        'name': 'ubuntu',
        'version': '20',
        'family': 'debian'
    }
    display.debug.assert_called()

def test_get_distribution_failed_module(monkeypatch, action_module, task_vars):
    display = MagicMock()
    monkeypatch.setattr('ansible.plugins.action.reboot.display', display)
    
    module_output = {
        'failed': True,
        'module_stdout': 'Some error',
        'module_stderr': 'Some stderr'
    }
    
    action_module._execute_module = MagicMock(return_value=module_output)
    
    with pytest.raises(AnsibleError, match='Failed to determine system distribution. Some error, Some stderr'):
        action_module.get_distribution(task_vars)
    
    display.debug.assert_called()

def test_get_distribution_key_error(monkeypatch, action_module, task_vars):
    display = MagicMock()
    monkeypatch.setattr('ansible.plugins.action.reboot.display', display)
    
    module_output = {
        'ansible_facts': {
            'ansible_distribution': 'Ubuntu',
            'ansible_distribution_version': '20.04'
        }
    }
    
    action_module._execute_module = MagicMock(return_value=module_output)
    
    with pytest.raises(AnsibleError, match='Failed to get distribution information. Missing "ansible_os_family" in output.'):
        action_module.get_distribution(task_vars)
    
    display.debug.assert_called()
