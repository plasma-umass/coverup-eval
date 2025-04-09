# file: lib/ansible/plugins/callback/default.py:222-223
# asked: {"lines": [222, 223], "branches": []}
# gained: {"lines": [222, 223], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_cleanup_task_start(callback_module, mocker):
    task = Mock()
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    
    mocker.patch.object(callback_module, '_task_start', wraps=callback_module._task_start)
    mocker.patch.object(callback_module, '_play', create=True)
    callback_module._play.strategy = 'linear'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True
    mocker.patch.object(callback_module, '_print_task_banner')

    callback_module.v2_playbook_on_cleanup_task_start(task)
    
    callback_module._task_start.assert_called_once_with(task, prefix='CLEANUP TASK')
    assert callback_module._last_task_name == 'Test Task'
    callback_module._print_task_banner.assert_called_once_with(task)
