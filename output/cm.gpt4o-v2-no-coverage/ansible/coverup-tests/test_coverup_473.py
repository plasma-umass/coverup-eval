# file: lib/ansible/vars/clean.py:167-176
# asked: {"lines": [167, 169, 170, 171, 172, 174, 176], "branches": [[170, 171], [170, 176], [171, 172], [171, 174]]}
# gained: {"lines": [167, 169, 170, 171, 172, 174, 176], "branches": [[170, 171], [170, 176], [171, 172], [171, 174]]}

import pytest
from ansible.vars.clean import namespace_facts, module_response_deepcopy

def test_namespace_facts():
    facts = {
        'ansible_os_family': 'Debian',
        'ansible_distribution': 'Ubuntu',
        'ansible_local': 'local_value',
        'other_fact': 'value'
    }
    
    expected_result = {
        'ansible_facts': {
            'os_family': 'Debian',
            'distribution': 'Ubuntu',
            'ansible_local': 'local_value',
            'other_fact': 'value'
        }
    }
    
    result = namespace_facts(facts)
    assert result == expected_result

def test_module_response_deepcopy_dict():
    data = {'key1': 'value1', 'key2': {'subkey': 'subvalue'}}
    result = module_response_deepcopy(data)
    assert result == data
    assert result is not data
    assert result['key2'] is not data['key2']

def test_module_response_deepcopy_list():
    data = ['value1', ['subvalue']]
    result = module_response_deepcopy(data)
    assert result == data
    assert result is not data
    assert result[1] is not data[1]

def test_module_response_deepcopy_other():
    data = 'string'
    result = module_response_deepcopy(data)
    assert result == data
    assert result is data
