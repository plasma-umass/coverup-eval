# file: lib/ansible/plugins/action/fail.py:24-43
# asked: {"lines": [24, 25, 27, 28, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43], "branches": [[31, 32], [31, 34], [38, 39], [38, 41]]}
# gained: {"lines": [24, 25, 27, 28, 30, 31, 34, 35, 37, 38, 39, 41, 42, 43], "branches": [[31, 34], [38, 39], [38, 41]]}

import pytest
from ansible.plugins.action.fail import ActionModule
from ansible.playbook.task import Task
from ansible.executor.task_result import TaskResult
from ansible.utils.vars import load_extra_vars
from ansible.module_utils.common.collections import ImmutableDict

@pytest.fixture
def action_module(mocker):
    task = Task.load(dict(action='fail', args=dict(msg='Custom failure message')))
    connection = mocker.Mock()
    play_context = mocker.Mock()
    loader = mocker.Mock()
    templar = mocker.Mock()
    shared_loader_obj = mocker.Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_action_module_run_with_msg(action_module, mocker):
    mocker.patch.object(ActionModule, 'run', wraps=action_module.run)
    result = action_module.run(task_vars={})
    assert result['failed'] is True
    assert result['msg'] == 'Custom failure message'

def test_action_module_run_without_msg(mocker):
    task = Task.load(dict(action='fail', args={}))
    connection = mocker.Mock()
    play_context = mocker.Mock()
    loader = mocker.Mock()
    templar = mocker.Mock()
    shared_loader_obj = mocker.Mock()
    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    mocker.patch.object(ActionModule, 'run', wraps=action_module.run)
    result = action_module.run(task_vars={})
    assert result['failed'] is True
    assert result['msg'] == 'Failed as requested from task'
