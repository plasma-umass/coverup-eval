# file: lib/ansible/plugins/action/fail.py:24-43
# asked: {"lines": [24, 25, 27, 28, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43], "branches": [[31, 32], [31, 34], [38, 39], [38, 41]]}
# gained: {"lines": [24, 25, 27, 28, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43], "branches": [[31, 32], [31, 34], [38, 39], [38, 41]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.fail import ActionModule
from ansible.errors import AnsibleActionFail

@pytest.fixture
def action_module():
    task = MagicMock()
    task.async_val = False
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_default_message(mock_run, action_module):
    action_module._task.args = {}
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == 'Failed as requested from task'
    mock_run.assert_called_once()

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_custom_message(mock_run, action_module):
    action_module._task.args = {'msg': 'Custom failure message'}
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == 'Custom failure message'
    mock_run.assert_called_once()

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_no_task_vars(mock_run, action_module):
    action_module._task.args = {}
    result = action_module.run(task_vars=None)
    assert result['failed'] is True
    assert result['msg'] == 'Failed as requested from task'
    mock_run.assert_called_once()

@patch('ansible.plugins.action.ActionBase.run', return_value={})
def test_run_with_task_vars(mock_run, action_module):
    action_module._task.args = {}
    result = action_module.run(task_vars={'some_var': 'some_value'})
    assert result['failed'] is True
    assert result['msg'] == 'Failed as requested from task'
    mock_run.assert_called_once()
