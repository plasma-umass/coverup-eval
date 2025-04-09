# file: lib/ansible/plugins/callback/junit.py:176-203
# asked: {"lines": [176, 179, 181, 182, 183, 185, 186, 188, 190, 191, 194, 195, 196, 197, 198, 199, 200, 202, 203], "branches": [[181, 182], [181, 185], [190, 191], [190, 194], [194, 195], [194, 196], [196, 197], [196, 202], [197, 198], [197, 199], [199, 200], [199, 202], [202, 0], [202, 203]]}
# gained: {"lines": [176, 179, 181, 182, 183, 185, 186, 188, 190, 191, 194, 195, 196, 197, 198, 199, 200, 202, 203], "branches": [[181, 182], [181, 185], [190, 191], [190, 194], [194, 195], [194, 196], [196, 197], [196, 202], [197, 198], [197, 199], [199, 200], [202, 203]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.junit import CallbackModule

class HostData:
    def __init__(self, host_uuid, host_name, status, result):
        self.host_uuid = host_uuid
        self.host_name = host_name
        self.status = status
        self.result = result

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_finish_task_with_host(callback_module):
    mock_task = Mock()
    mock_task._uuid = 'task-uuid'
    mock_result = Mock()
    mock_result._task = mock_task
    mock_result._host._uuid = 'host-uuid'
    mock_result._host.name = 'host-name'
    mock_result._result = {}

    task_data = Mock()
    task_data.name = 'task-name'
    callback_module._task_data = {
        'task-uuid': task_data
    }

    callback_module._finish_task('ok', mock_result)

    assert callback_module._task_data['task-uuid'].add_host.called

def test_finish_task_without_host(callback_module):
    mock_task = Mock()
    mock_task._uuid = 'task-uuid'
    mock_result = Mock()
    mock_result._task = mock_task
    del mock_result._host
    mock_result._result = {}

    task_data = Mock()
    task_data.name = 'task-name'
    callback_module._task_data = {
        'task-uuid': task_data
    }

    callback_module._finish_task('ok', mock_result)

    assert callback_module._task_data['task-uuid'].add_host.called

def test_finish_task_fail_on_change(callback_module, monkeypatch):
    monkeypatch.setattr(callback_module, '_fail_on_change', 'true')
    mock_task = Mock()
    mock_task._uuid = 'task-uuid'
    mock_result = Mock()
    mock_result._task = mock_task
    mock_result._host._uuid = 'host-uuid'
    mock_result._host.name = 'host-name'
    mock_result._result = {'changed': True}

    task_data = Mock()
    task_data.name = 'task-name'
    callback_module._task_data = {
        'task-uuid': task_data
    }

    callback_module._finish_task('ok', mock_result)

    assert callback_module._task_data['task-uuid'].add_host.called

def test_finish_task_expected_failure(callback_module):
    mock_task = Mock()
    mock_task._uuid = 'task-uuid'
    mock_result = Mock()
    mock_result._task = mock_task
    mock_result._host._uuid = 'host-uuid'
    mock_result._host.name = 'host-name'
    mock_result._result = {}

    task_data = Mock()
    task_data.name = 'EXPECTED FAILURE'
    callback_module._task_data = {
        'task-uuid': task_data
    }

    callback_module._finish_task('failed', mock_result)

    assert callback_module._task_data['task-uuid'].add_host.called

def test_finish_task_toggle_result(callback_module):
    mock_task = Mock()
    mock_task._uuid = 'task-uuid'
    mock_result = Mock()
    mock_result._task = mock_task
    mock_result._host._uuid = 'host-uuid'
    mock_result._host.name = 'host-name'
    mock_result._result = {}

    task_data = Mock()
    task_data.name = 'TOGGLE RESULT'
    callback_module._task_data = {
        'task-uuid': task_data
    }

    callback_module._finish_task('failed', mock_result)
    assert callback_module._task_data['task-uuid'].add_host.called

    callback_module._finish_task('ok', mock_result)
    assert callback_module._task_data['task-uuid'].add_host.called

def test_finish_task_with_test_case_prefix(callback_module, monkeypatch):
    monkeypatch.setattr(callback_module, '_test_case_prefix', 'test_')
    mock_task = Mock()
    mock_task._uuid = 'task-uuid'
    mock_result = Mock()
    mock_result._task = mock_task
    mock_result._host._uuid = 'host-uuid'
    mock_result._host.name = 'host-name'
    mock_result._result = {}

    task_data = Mock()
    task_data.name = 'test_case'
    callback_module._task_data = {
        'task-uuid': task_data
    }

    callback_module._finish_task('ok', mock_result)
    assert callback_module._task_data['task-uuid'].add_host.called
