# file: lib/ansible/plugins/action/group_by.py:24-51
# asked: {"lines": [24, 25, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51], "branches": [[32, 33], [32, 35], [38, 39], [38, 43], [45, 46], [45, 48]]}
# gained: {"lines": [24, 25, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51], "branches": [[32, 33], [38, 39], [38, 43], [45, 46], [45, 48]]}

import pytest
from ansible.plugins.action.group_by import ActionModule
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    play_context = PlayContext()
    task = Task()
    connection = MagicMock()
    loader = MagicMock()
    return ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=None,
        shared_loader_obj=None,
    )

def test_run_no_key(action_module):
    action_module._task.args = {}
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == "the 'key' param is required when using group_by"

def test_run_with_key_and_parents(action_module):
    action_module._task.args = {'key': 'test_group', 'parents': 'parent_group'}
    result = action_module.run()
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group']

def test_run_with_key_and_multiple_parents(action_module):
    action_module._task.args = {'key': 'test_group', 'parents': ['parent_group1', 'parent_group2']}
    result = action_module.run()
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group1', 'parent_group2']

def test_run_with_key_and_parents_as_string(action_module):
    action_module._task.args = {'key': 'test_group', 'parents': 'parent_group'}
    result = action_module.run()
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group']

def test_run_with_key_and_default_parents(action_module):
    action_module._task.args = {'key': 'test group'}
    result = action_module.run()
    assert result['changed'] is False
    assert result['add_group'] == 'test-group'
    assert result['parent_groups'] == ['all']
