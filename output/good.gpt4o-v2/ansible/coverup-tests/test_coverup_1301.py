# file: lib/ansible/plugins/callback/junit.py:304-305
# asked: {"lines": [305], "branches": []}
# gained: {"lines": [305], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_skipped(callback_module, mocker):
    result = MagicMock()
    result._task._uuid = 'task-uuid'
    result._host._uuid = 'host-uuid'
    result._host.name = 'host-name'
    result._result.get.return_value = False

    mocker.patch.object(callback_module, '_finish_task')
    mocker.patch.object(callback_module, '_task_data', {'task-uuid': MagicMock()})
    mocker.patch.object(callback_module, '_fail_on_change', 'false')
    mocker.patch.object(callback_module, '_test_case_prefix', '')

    callback_module.v2_runner_on_skipped(result)

    callback_module._finish_task.assert_called_once_with('skipped', result)
