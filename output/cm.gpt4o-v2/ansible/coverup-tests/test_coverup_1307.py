# file: lib/ansible/plugins/callback/junit.py:301-302
# asked: {"lines": [302], "branches": []}
# gained: {"lines": [302], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.junit import CallbackModule, HostData, TaskData

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_ok(callback_module, mocker):
    # Mock the result object
    result = Mock()
    result._task._uuid = 'task-uuid'
    result._host._uuid = 'host-uuid'
    result._host.name = 'host-name'
    result._result = {'changed': False}

    # Mock the necessary attributes and methods
    task_data = Mock(spec=TaskData)
    task_data.name = 'test-task'
    callback_module._task_data = {
        'task-uuid': task_data
    }
    callback_module._fail_on_change = 'false'
    callback_module._test_case_prefix = 'test-'

    # Call the method
    callback_module.v2_runner_on_ok(result)

    # Assertions to verify the behavior
    callback_module._task_data['task-uuid'].add_host.assert_called_once()
    host_data = callback_module._task_data['task-uuid'].add_host.call_args[0][0]
    assert host_data.uuid == 'host-uuid'
    assert host_data.name == 'host-name'
    assert host_data.status == 'ok'
    assert host_data.result == result
