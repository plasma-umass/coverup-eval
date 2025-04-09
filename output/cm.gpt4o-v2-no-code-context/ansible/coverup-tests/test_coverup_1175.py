# file: lib/ansible/plugins/action/gather_facts.py:55-63
# asked: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}
# gained: {"lines": [55, 56, 57, 58, 59, 63], "branches": []}

import pytest
from ansible.plugins.action.gather_facts import ActionModule
from ansible.utils.vars import merge_hash

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_combine_task_result_with_facts(action_module, mocker):
    result = {'ansible_facts': {'existing_fact': 'value1'}, 'warnings': ['existing_warning'], 'deprecations': ['existing_deprecation']}
    task_result = {'ansible_facts': {'new_fact': 'value2'}, 'warnings': ['new_warning'], 'deprecations': ['new_deprecation']}
    
    mock_merge_hash = mocker.patch('ansible.plugins.action.gather_facts.merge_hash', wraps=merge_hash)
    
    combined_result = action_module._combine_task_result(result, task_result)
    
    expected_result = {
        'ansible_facts': {'existing_fact': 'value1', 'new_fact': 'value2'},
        'warnings': ['existing_warning', 'new_warning'],
        'deprecations': ['existing_deprecation', 'new_deprecation']
    }
    
    mock_merge_hash.assert_called_once_with(result, {
        'ansible_facts': {'new_fact': 'value2'},
        'warnings': ['new_warning'],
        'deprecations': ['new_deprecation']
    }, list_merge='append_rp')
    
    assert combined_result == expected_result

def test_combine_task_result_without_facts(action_module, mocker):
    result = {'ansible_facts': {'existing_fact': 'value1'}, 'warnings': ['existing_warning'], 'deprecations': ['existing_deprecation']}
    task_result = {}
    
    mock_merge_hash = mocker.patch('ansible.plugins.action.gather_facts.merge_hash', wraps=merge_hash)
    
    combined_result = action_module._combine_task_result(result, task_result)
    
    expected_result = {
        'ansible_facts': {'existing_fact': 'value1'},
        'warnings': ['existing_warning'],
        'deprecations': ['existing_deprecation']
    }
    
    mock_merge_hash.assert_called_once_with(result, {
        'ansible_facts': {},
        'warnings': [],
        'deprecations': []
    }, list_merge='append_rp')
    
    assert combined_result == expected_result
