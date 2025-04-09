# file lib/ansible/plugins/callback/default.py:101-134
# lines [101, 103, 105, 106, 107, 108, 109, 110, 111, 113, 114, 116, 117, 119, 120, 122, 123, 125, 127, 128, 130, 132, 133, 134]
# branches ['105->106', '105->109', '106->107', '106->108', '109->110', '109->116', '110->111', '110->113', '116->117', '116->119', '119->120', '119->122', '127->128', '127->130', '132->133', '132->134']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task
from unittest.mock import MagicMock, patch

class FakeTask(Task):
    def __init__(self, action, uuid):
        super(FakeTask, self).__init__()
        self.action = action
        self._uuid = uuid

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def task_result():
    fake_loader = MagicMock()
    fake_loader.get_basedir.return_value = ''
    task = FakeTask(action='fake_action', uuid='fake_uuid')
    host = MagicMock()
    host.name = 'fake_host'
    host.get_name.return_value = 'fake_host'
    return TaskResult(host=host, task=task, return_data={})

def test_v2_runner_on_ok_with_changed_result(callback_module, task_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_process_items')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')

    task_result._result['changed'] = True
    task_result._task._uuid = 'different_uuid'

    callback_module.v2_runner_on_ok(task_result)

    callback_module._print_task_banner.assert_called_once_with(task_result._task)
    callback_module._handle_warnings.assert_called_once_with(task_result._result)
    callback_module._clean_results.assert_called_once_with(task_result._result, task_result._task.action)
    callback_module._display.display.assert_called_once_with('changed: [fake_host]', color='yellow')

def test_v2_runner_on_ok_with_include_task(callback_module, task_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_process_items')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')

    task_result._task = TaskInclude()
    task_result._task._uuid = 'fake_uuid'
    callback_module._last_task_banner = 'fake_uuid'

    callback_module.v2_runner_on_ok(task_result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._handle_warnings.assert_not_called()
    callback_module._process_items.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._display.display.assert_not_called()

def test_v2_runner_on_ok_with_ok_result_and_display_ok_hosts(callback_module, task_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_process_items')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')

    callback_module.display_ok_hosts = True
    task_result._result['changed'] = False
    task_result._task._uuid = 'different_uuid'

    callback_module.v2_runner_on_ok(task_result)

    callback_module._print_task_banner.assert_called_once_with(task_result._task)
    callback_module._handle_warnings.assert_called_once_with(task_result._result)
    callback_module._clean_results.assert_called_once_with(task_result._result, task_result._task.action)
    callback_module._display.display.assert_called_once_with('ok: [fake_host]', color='green')
