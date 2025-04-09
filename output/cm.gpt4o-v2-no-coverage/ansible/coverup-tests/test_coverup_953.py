# file: lib/ansible/plugins/callback/default.py:225-226
# asked: {"lines": [225, 226], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_handler_task_start(callback_module, mocker):
    task = Mock()
    task._uuid = '1234'
    task.get_name.return_value = 'Test Task'
    
    mocker.patch.object(callback_module, '_task_type_cache', {})
    mocker.patch.object(callback_module, '_play', Mock(strategy='linear'))
    mocker.patch.object(callback_module, '_print_task_banner')
    
    # Manually set attributes since they are not defined in the class
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True

    callback_module.v2_playbook_on_handler_task_start(task)

    assert callback_module._task_type_cache[task._uuid] == 'RUNNING HANDLER'
    assert callback_module._last_task_name == 'Test Task'
    callback_module._print_task_banner.assert_called_once_with(task)
