# file: lib/ansible/vars/clean.py:167-176
# asked: {"lines": [167, 169, 170, 171, 172, 174, 176], "branches": [[170, 171], [170, 176], [171, 172], [171, 174]]}
# gained: {"lines": [167, 169, 170, 171, 172, 174, 176], "branches": [[170, 171], [170, 176], [171, 172], [171, 174]]}

import pytest
from ansible.vars.clean import namespace_facts

def test_namespace_facts_with_ansible_prefix(mocker):
    facts = {
        'ansible_os_family': 'Debian',
        'ansible_local': 'local_value',
        'other_fact': 'value'
    }
    
    mock_deepcopy = mocker.patch('ansible.vars.clean.module_response_deepcopy', side_effect=lambda x: x)
    
    result = namespace_facts(facts)
    
    expected = {
        'ansible_facts': {
            'os_family': 'Debian',
            'ansible_local': 'local_value',
            'other_fact': 'value'
        }
    }
    
    assert result == expected
    mock_deepcopy.assert_any_call('Debian')
    mock_deepcopy.assert_any_call('local_value')
    mock_deepcopy.assert_any_call('value')

def test_namespace_facts_without_ansible_prefix(mocker):
    facts = {
        'os_family': 'Debian',
        'other_fact': 'value'
    }
    
    mock_deepcopy = mocker.patch('ansible.vars.clean.module_response_deepcopy', side_effect=lambda x: x)
    
    result = namespace_facts(facts)
    
    expected = {
        'ansible_facts': {
            'os_family': 'Debian',
            'other_fact': 'value'
        }
    }
    
    assert result == expected
    mock_deepcopy.assert_any_call('Debian')
    mock_deepcopy.assert_any_call('value')
