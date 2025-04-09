# file lib/ansible/plugins/callback/default.py:78-99
# lines [80, 81, 83, 84, 86, 87, 89, 90, 93, 94, 95, 96, 98, 99]
# branches ['83->84', '83->86', '89->90', '89->93', '93->94', '93->95', '98->exit', '98->99']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch

# Mock constants that are not available in this context
class C:
    COLOR_ERROR = 'red'
    COLOR_SKIP = 'yellow'

@pytest.fixture
def callback_module(mocker):
    mocker.patch('ansible.plugins.callback.default.C', new=C)
    display = Display()
    mocker.patch.object(display, 'display')
    callback_module = CallbackModule()
    callback_module._display = display
    callback_module._last_task_banner = None
    callback_module._plugin_options = {'show_task_path_on_failure': True}
    callback_module.display_failed_stderr = False  # Add the missing attribute
    return callback_module

@pytest.fixture
def task_result(mocker):
    fake_loader = DataLoader()
    task = Task()
    task._uuid = '1234-5678'
    task.action = 'fake_action'
    task.args = {}
    task.get_path = lambda: '/fake/path'
    result = TaskResult(host='localhost', task=task, return_data={
        '_ansible_verbose_always': True,
        '_ansible_no_log': False,
    })
    result._result = {'failed': True, 'msg': 'Test failure'}
    result._task = task
    return result

def test_v2_runner_on_failed_with_ignore_errors(callback_module, task_result, mocker):
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_print_task_path')
    mocker.patch.object(callback_module, '_dump_results', return_value='{}')
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')

    callback_module.v2_runner_on_failed(task_result, ignore_errors=True)

    # Assertions to check if the lines 80-99 are covered
    callback_module._clean_results.assert_called_once_with(task_result._result, task_result._task.action)
    callback_module._print_task_banner.assert_called_once_with(task_result._task)
    callback_module._handle_exception.assert_called_once_with(task_result._result, use_stderr=callback_module.display_failed_stderr)
    callback_module._handle_warnings.assert_called_once_with(task_result._result)
    callback_module._print_task_path.assert_called_once_with(task_result._task)
    callback_module._dump_results.assert_called_once_with(task_result._result)
    callback_module._display.display.assert_any_call("fatal: [localhost]: FAILED! => {}", color=C.COLOR_ERROR, stderr=callback_module.display_failed_stderr)
    callback_module._display.display.assert_any_call("...ignoring", color=C.COLOR_SKIP)
