# file: lib/ansible/plugins/action/gather_facts.py:55-63
# asked: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}
# gained: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}

import pytest
from ansible.plugins.action.gather_facts import ActionModule
from ansible.utils.vars import merge_hash

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_combine_task_result(action_module, mocker):
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

    expected_result = {
        'ansible_facts': {'fact1': 'value1', 'fact2': 'value2'},
        'warnings': ['warning1', 'warning2'],
        'deprecations': ['deprecation1', 'deprecation2']
    }

    mocker.patch('ansible.utils.vars.merge_hash', side_effect=merge_hash)
    combined_result = action_module._combine_task_result(result, task_result)
    
    assert combined_result == expected_result
