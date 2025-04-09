# file lib/ansible/plugins/action/fail.py:24-43
# lines [24, 25, 27, 28, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43]
# branches ['31->32', '31->34', '38->39', '38->41']

import pytest
from ansible.plugins.action.fail import ActionModule
from ansible.executor.task_executor import TaskExecutor
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.template import Templar
from unittest.mock import MagicMock, create_autospec

@pytest.fixture
def mock_task_executor(mocker):
    executor = create_autospec(TaskExecutor)
    executor._job_vars = {}
    executor._play_context = MagicMock()
    executor._play_context.check_mode = False
    executor._play_context.diff = False
    executor._play_context.verbosity = 0
    executor._play_context.connection = 'local'
    executor._play_context.remote_addr = 'localhost'
    executor._play_context.passwords = {}
    executor._loader = MagicMock()
    executor._templar = Templar(loader=executor._loader)
    executor._task = Task()
    executor._task.action = 'fail'
    return executor

@pytest.fixture
def action_module(mock_task_executor):
    return ActionModule(task=mock_task_executor._task, connection=MagicMock(), play_context=mock_task_executor._play_context, loader=mock_task_executor._loader, templar=mock_task_executor._templar, shared_loader_obj=MagicMock())

def test_fail_module_with_custom_message(action_module):
    # Set custom message
    custom_message = "Custom failure message"
    action_module._task.args = {'msg': custom_message}
    
    # Run the action module
    result = action_module.run(task_vars={})
    
    # Assert the result
    assert result['failed'] is True
    assert result['msg'] == custom_message

def test_fail_module_with_default_message(action_module):
    # Ensure no custom message is set
    action_module._task.args = {}
    
    # Run the action module
    result = action_module.run(task_vars={})
    
    # Assert the result
    assert result['failed'] is True
    assert result['msg'] == "Failed as requested from task"
