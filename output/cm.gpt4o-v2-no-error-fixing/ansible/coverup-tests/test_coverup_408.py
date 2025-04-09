# file: lib/ansible/plugins/action/gather_facts.py:55-63
# asked: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}
# gained: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}

import pytest
from ansible.plugins.action.gather_facts import ActionModule
from ansible.utils.vars import merge_hash

class MockTask:
    def __init__(self):
        self.args = {}

class MockConnection:
    pass

class MockPlayContext:
    pass

class MockLoader:
    pass

class MockTemplar:
    pass

class MockSharedLoaderObj:
    pass

@pytest.fixture
def action_module():
    task = MockTask()
    connection = MockConnection()
    play_context = MockPlayContext()
    loader = MockLoader()
    templar = MockTemplar()
    shared_loader_obj = MockSharedLoaderObj()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_combine_task_result(action_module):
    result = {
        'ansible_facts': {'fact1': 'value1'},
        'warnings': ['warning1'],
        'deprecations': ['deprecation1']
    }
    task_result = {
        'ansible_facts': {'fact2': 'value2'},
        'warnings': ['warning2'],
        'deprecations': ['deprecation2']
    }
    combined_result = action_module._combine_task_result(result, task_result)
    
    expected_result = {
        'ansible_facts': {'fact1': 'value1', 'fact2': 'value2'},
        'warnings': ['warning1', 'warning2'],
        'deprecations': ['deprecation1', 'deprecation2']
    }
    
    assert combined_result == expected_result
