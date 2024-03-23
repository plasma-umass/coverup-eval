# file lib/ansible/vars/clean.py:167-176
# lines [167, 169, 170, 171, 172, 174, 176]
# branches ['170->171', '170->176', '171->172', '171->174']

import pytest
from ansible.vars.clean import namespace_facts

def test_namespace_facts_with_ansible_prefix(mocker):
    # Mock the module_response_deepcopy to simply return the value passed to it
    mocker.patch('ansible.vars.clean.module_response_deepcopy', side_effect=lambda x: x)

    facts = {
        'ansible_os_family': 'Debian',
        'ansible_local': {},
        'non_ansible_var': 'value'
    }

    expected = {
        'ansible_facts': {
            'os_family': 'Debian',
            'ansible_local': {},
            'non_ansible_var': 'value'
        }
    }

    result = namespace_facts(facts)
    assert result == expected

def test_namespace_facts_without_ansible_prefix(mocker):
    # Mock the module_response_deepcopy to simply return the value passed to it
    mocker.patch('ansible.vars.clean.module_response_deepcopy', side_effect=lambda x: x)

    facts = {
        'non_ansible_var': 'value'
    }

    expected = {
        'ansible_facts': {
            'non_ansible_var': 'value'
        }
    }

    result = namespace_facts(facts)
    assert result == expected
