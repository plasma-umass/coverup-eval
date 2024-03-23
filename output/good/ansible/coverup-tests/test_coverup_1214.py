# file lib/ansible/plugins/callback/default.py:136-151
# lines [138, 140, 142, 143, 145, 146, 148, 149, 150, 151]
# branches ['138->exit', '138->140', '142->143', '142->145', '145->146', '145->148', '149->150', '149->151']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from unittest.mock import MagicMock, patch

@pytest.fixture
def callback_module():
    callback = CallbackModule()
    callback._display = MagicMock()
    callback._display.verbosity = 0  # Set verbosity to an integer value
    callback._last_task_banner = None
    callback.display_skipped_hosts = True
    callback.check_mode_markers = False
    callback._task_type_cache = {}
    callback._last_task_name = None
    return callback

@pytest.fixture
def task_result():
    fake_task = MagicMock(Task)
    fake_task._uuid = 'fake_uuid'
    fake_host = MagicMock()
    fake_host.get_name.return_value = 'fake_host'
    fake_result = {'skipped': True, 'msg': 'fake_reason'}
    result = TaskResult(host=fake_host, task=fake_task, return_data=fake_result)
    return result

def test_v2_runner_on_skipped_with_loop(callback_module, task_result):
    task_result._task.loop = True
    task_result._result['results'] = [{'skipped': True, 'msg': 'fake_reason'}]

    with patch.object(callback_module, '_process_items') as mock_process_items:
        callback_module.v2_runner_on_skipped(task_result)
        mock_process_items.assert_called_once_with(task_result)

def test_v2_runner_on_skipped_without_loop(callback_module, task_result):
    task_result._task.loop = False

    with patch.object(callback_module, '_run_is_verbose') as mock_run_is_verbose:
        mock_run_is_verbose.return_value = False
        callback_module.v2_runner_on_skipped(task_result)
        callback_module._display.display.assert_called_once_with(
            "skipping: [fake_host]", color='cyan'
        )

def test_v2_runner_on_skipped_with_verbose(callback_module, task_result):
    task_result._task.loop = False

    with patch.object(callback_module, '_run_is_verbose') as mock_run_is_verbose, \
         patch.object(callback_module, '_dump_results') as mock_dump_results:
        mock_run_is_verbose.return_value = True
        mock_dump_results.return_value = 'fake_dump'
        callback_module.v2_runner_on_skipped(task_result)
        callback_module._display.display.assert_called_once_with(
            "skipping: [fake_host] => fake_dump", color='cyan'
        )
