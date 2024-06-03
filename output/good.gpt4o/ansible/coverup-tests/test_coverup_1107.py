# file lib/ansible/plugins/callback/default.py:136-151
# lines [138, 140, 142, 143, 145, 146, 148, 149, 150, 151]
# branches ['138->exit', '138->140', '142->143', '142->145', '145->146', '145->148', '149->150', '149->151']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.inventory.host import Host
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_skipped_hosts = True
    module._last_task_banner = None
    module._display = MagicMock()
    return module

@pytest.fixture
def result():
    task = Task()
    task._uuid = "1234"
    task.action = "test_action"
    task.loop = None
    host = Host(name="test_host")
    return TaskResult(host=host, task=task, return_data={"skipped": True})

def test_v2_runner_on_skipped(callback_module, result):
    with patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_run_is_verbose', return_value=True) as mock_run_is_verbose, \
         patch.object(callback_module, '_dump_results', return_value="dumped_results") as mock_dump_results:
        
        callback_module.v2_runner_on_skipped(result)
        
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        mock_print_task_banner.assert_called_once_with(result._task)
        mock_run_is_verbose.assert_called_once_with(result)
        mock_dump_results.assert_called_once_with(result._result)
        callback_module._display.display.assert_called_once_with("skipping: [test_host] => dumped_results", color=C.COLOR_SKIP)
