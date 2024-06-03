# file lib/ansible/plugins/callback/default.py:263-288
# lines [276, 287]
# branches ['269->272', '275->276', '278->281', '286->287']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_task():
    task = MagicMock()
    task._uuid = 'test-uuid'
    return task

@pytest.fixture
def mock_result(mock_task):
    result = MagicMock(spec=TaskResult)
    result._task = mock_task
    result._result = {'changed': True}
    result._host = MagicMock()
    result._host.get_name.return_value = 'test-host'
    return result

def test_v2_runner_item_on_ok_changed(callback_module, mock_result):
    mock_result._result['changed'] = True
    callback_module._last_task_banner = 'different-uuid'
    callback_module._print_task_banner = MagicMock()
    callback_module._clean_results = MagicMock()
    callback_module._run_is_verbose = MagicMock(return_value=False)
    callback_module._display.display = MagicMock()

    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._display.display.assert_called_once()
    assert 'changed' in callback_module._display.display.call_args[0][0]

def test_v2_runner_item_on_ok_ok(callback_module, mock_result):
    mock_result._result['changed'] = False
    callback_module.display_ok_hosts = True
    callback_module._last_task_banner = 'different-uuid'
    callback_module._print_task_banner = MagicMock()
    callback_module._clean_results = MagicMock()
    callback_module._run_is_verbose = MagicMock(return_value=False)
    callback_module._display.display = MagicMock()

    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._display.display.assert_called_once()
    assert 'ok' in callback_module._display.display.call_args[0][0]

def test_v2_runner_item_on_ok_verbose(callback_module, mock_result):
    mock_result._result['changed'] = True
    callback_module._last_task_banner = 'test-uuid'
    callback_module._print_task_banner = MagicMock()
    callback_module._clean_results = MagicMock()
    callback_module._run_is_verbose = MagicMock(return_value=True)
    callback_module._dump_results = MagicMock(return_value='dumped results')
    callback_module._display.display = MagicMock()

    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._display.display.assert_called_once()
    assert 'changed' in callback_module._display.display.call_args[0][0]
    assert 'dumped results' in callback_module._display.display.call_args[0][0]

def test_v2_runner_item_on_ok_no_display_ok_hosts(callback_module, mock_result):
    mock_result._result['changed'] = False
    callback_module.display_ok_hosts = False
    callback_module._last_task_banner = 'test-uuid'
    callback_module._print_task_banner = MagicMock()
    callback_module._clean_results = MagicMock()
    callback_module._run_is_verbose = MagicMock(return_value=False)
    callback_module._display.display = MagicMock()

    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._display.display.assert_not_called()
