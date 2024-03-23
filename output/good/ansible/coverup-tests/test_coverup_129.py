# file lib/ansible/plugins/action/group_by.py:24-51
# lines [24, 25, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51]
# branches ['32->33', '32->35', '38->39', '38->43', '45->46', '45->48']

import pytest
from ansible.plugins.action.group_by import ActionModule
from ansible.utils.sentinel import Sentinel
from ansible.module_utils.six import string_types

# Mock the ActionBase class
class MockActionBase:
    def run(self, tmp=None, task_vars=None):
        return {}

# Mock the ActionModule class to inherit from MockActionBase instead of ActionBase
ActionModule.__bases__ = (MockActionBase,)

@pytest.fixture
def action_module(mocker):
    mocker.patch('ansible.plugins.action.ActionBase.run', return_value={})
    action_module = ActionModule()
    action_module._task = mocker.MagicMock()
    action_module._connection = mocker.MagicMock()
    action_module._play_context = mocker.MagicMock()
    action_module._loader = mocker.MagicMock()
    action_module._templar = mocker.MagicMock()
    action_module._shared_loader_obj = mocker.MagicMock()
    return action_module

def test_group_by_key_not_provided(action_module):
    result = action_module.run(task_vars={})
    assert result['failed']
    assert result['msg'] == "the 'key' param is required when using group_by"

def test_group_by_with_key_and_default_parents(action_module):
    action_module._task.args = {'key': 'test_group'}
    result = action_module.run(task_vars={})
    assert 'failed' not in result
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['all']

def test_group_by_with_key_and_custom_parents_string(action_module):
    action_module._task.args = {'key': 'test_group', 'parents': 'custom_parent'}
    result = action_module.run(task_vars={})
    assert 'failed' not in result
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['custom_parent']

def test_group_by_with_key_and_custom_parents_list(action_module):
    action_module._task.args = {'key': 'test_group', 'parents': ['custom_parent1', 'custom_parent2']}
    result = action_module.run(task_vars={})
    assert 'failed' not in result
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['custom_parent1', 'custom_parent2']

def test_group_by_with_key_and_custom_parents_with_spaces(action_module):
    action_module._task.args = {'key': 'test group', 'parents': ['custom parent1', 'custom parent2']}
    result = action_module.run(task_vars={})
    assert 'failed' not in result
    assert result['add_group'] == 'test-group'
    assert result['parent_groups'] == ['custom-parent1', 'custom-parent2']
