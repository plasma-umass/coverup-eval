# file lib/ansible/plugins/action/reboot.py:137-156
# lines [137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]
# branches ['146->147', '146->150']

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display

@pytest.fixture
def mock_display():
    with patch('ansible.plugins.action.reboot.display', autospec=True) as mock_display:
        yield mock_display

@pytest.fixture
def mock_execute_module():
    with patch.object(ActionModule, '_execute_module', autospec=True) as mock_execute_module:
        yield mock_execute_module

@pytest.fixture
def mock_task():
    task = MagicMock()
    task.action = 'reboot'
    return task

def test_get_distribution_success(mock_execute_module, mock_display, mock_task):
    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    mock_execute_module.return_value = {
        'ansible_facts': {
            'ansible_distribution': 'Ubuntu',
            'ansible_distribution_version': '20.04',
            'ansible_os_family': 'Debian'
        }
    }
    task_vars = {}

    distribution = action_module.get_distribution(task_vars)

    assert distribution['name'] == 'ubuntu'
    assert distribution['version'] == '20'
    assert distribution['family'] == 'debian'
    mock_display.debug.assert_called()

def test_get_distribution_failure(mock_execute_module, mock_display, mock_task):
    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    mock_execute_module.return_value = {
        'failed': True,
        'module_stdout': 'Some error',
        'module_stderr': 'Some stderr'
    }
    task_vars = {}

    with pytest.raises(AnsibleError, match='Failed to determine system distribution'):
        action_module.get_distribution(task_vars)

def test_get_distribution_key_error(mock_execute_module, mock_display, mock_task):
    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    mock_execute_module.return_value = {
        'ansible_facts': {
            'ansible_distribution': 'Ubuntu',
            'ansible_distribution_version': '20.04'
            # Missing 'ansible_os_family'
        }
    }
    task_vars = {}

    with pytest.raises(AnsibleError, match='Failed to get distribution information. Missing "ansible_os_family" in output.'):
        action_module.get_distribution(task_vars)
