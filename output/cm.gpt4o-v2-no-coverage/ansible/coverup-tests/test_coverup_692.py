# file: lib/ansible/plugins/action/gather_facts.py:55-63
# asked: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}
# gained: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}

import pytest
from ansible.plugins.action.gather_facts import ActionModule
from ansible.utils.vars import merge_hash
from ansible.plugins.action import ActionBase

class MockActionBase(ActionBase):
    def __init__(self):
        pass

    def run(self, tmp=None, task_vars=None):
        pass

@pytest.fixture
def action_module():
    return ActionModule(MockActionBase(), None, None, None, None, None)

def test_combine_task_result_empty(action_module):
    result = {}
    task_result = {}
    combined_result = action_module._combine_task_result(result, task_result)
    assert combined_result == {'ansible_facts': {}, 'warnings': [], 'deprecations': []}

def test_combine_task_result_with_data(action_module):
    result = {'ansible_facts': {'fact1': 'value1'}, 'warnings': ['warn1'], 'deprecations': ['dep1']}
    task_result = {'ansible_facts': {'fact2': 'value2'}, 'warnings': ['warn2'], 'deprecations': ['dep2']}
    combined_result = action_module._combine_task_result(result, task_result)
    assert combined_result == {
        'ansible_facts': {'fact1': 'value1', 'fact2': 'value2'},
        'warnings': ['warn1', 'warn2'],
        'deprecations': ['dep1', 'dep2']
    }

def test_combine_task_result_conflict(action_module):
    result = {'ansible_facts': {'fact1': 'value1'}, 'warnings': ['warn1'], 'deprecations': ['dep1']}
    task_result = {'ansible_facts': {'fact1': 'new_value1'}, 'warnings': ['warn2'], 'deprecations': ['dep2']}
    combined_result = action_module._combine_task_result(result, task_result)
    assert combined_result == {
        'ansible_facts': {'fact1': 'new_value1'},
        'warnings': ['warn1', 'warn2'],
        'deprecations': ['dep1', 'dep2']
    }
