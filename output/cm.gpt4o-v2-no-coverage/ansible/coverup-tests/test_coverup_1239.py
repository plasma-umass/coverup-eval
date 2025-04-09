# file: lib/ansible/plugins/callback/default.py:167-168
# asked: {"lines": [168], "branches": []}
# gained: {"lines": [168], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_task_start(callback_module, mocker):
    task = Mock()
    task.get_name.return_value = "Test Task"
    task._uuid = "1234"
    
    mocker.patch.object(callback_module, '_task_type_cache', {})
    mocker.patch.object(callback_module, '_play', Mock(strategy='linear'))
    mocker.patch.object(callback_module, 'display_skipped_hosts', True, create=True)
    mocker.patch.object(callback_module, 'display_ok_hosts', True, create=True)
    mocker.patch.object(callback_module, '_print_task_banner')

    callback_module.v2_playbook_on_task_start(task, is_conditional=False)

    assert callback_module._task_type_cache[task._uuid] == 'TASK'
    assert callback_module._last_task_name == "Test Task"
    callback_module._print_task_banner.assert_called_once_with(task)
