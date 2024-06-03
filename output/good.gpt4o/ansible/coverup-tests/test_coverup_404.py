# file lib/ansible/vars/clean.py:167-176
# lines [167, 169, 170, 171, 172, 174, 176]
# branches ['170->171', '170->176', '171->172', '171->174']

import pytest
from ansible.vars.clean import namespace_facts

def module_response_deepcopy(value):
    # Mock implementation of module_response_deepcopy
    if isinstance(value, dict):
        return value.copy()
    return value

@pytest.fixture
def mock_module_response_deepcopy(mocker):
    return mocker.patch('ansible.vars.clean.module_response_deepcopy', side_effect=module_response_deepcopy)

def test_namespace_facts(mock_module_response_deepcopy):
    facts = {
        'ansible_os_family': 'Debian',
        'ansible_distribution': 'Ubuntu',
        'ansible_local': 'local_value',
        'custom_fact': 'custom_value'
    }
    
    expected_result = {
        'ansible_facts': {
            'os_family': 'Debian',
            'distribution': 'Ubuntu',
            'ansible_local': 'local_value',
            'custom_fact': 'custom_value'
        }
    }
    
    result = namespace_facts(facts)
    assert result == expected_result
    assert mock_module_response_deepcopy.call_count == len(facts)
