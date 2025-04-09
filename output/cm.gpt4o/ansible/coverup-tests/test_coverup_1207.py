# file lib/ansible/plugins/action/gather_facts.py:55-63
# lines [55, 56, 57, 58, 59, 63]
# branches []

import pytest
from unittest.mock import Mock
from ansible.plugins.action.gather_facts import ActionModule
from ansible.utils.vars import merge_hash

@pytest.fixture
def action_module():
    return ActionModule(Mock(), Mock(), Mock(), Mock(), Mock(), Mock())

def test_combine_task_result(action_module, mocker):
    # Mocking merge_hash to ensure it is called correctly
    mock_merge_hash = mocker.patch('ansible.plugins.action.gather_facts.merge_hash', wraps=merge_hash)
    
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
    mock_merge_hash.assert_called_once_with(result, {
        'ansible_facts': {'fact2': 'value2'},
        'warnings': ['warning2'],
        'deprecations': ['deprecation2']
    }, list_merge='append_rp')
