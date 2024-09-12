# file: lib/ansible/vars/clean.py:167-176
# asked: {"lines": [167, 169, 170, 171, 172, 174, 176], "branches": [[170, 171], [170, 176], [171, 172], [171, 174]]}
# gained: {"lines": [167, 169, 170, 171, 172, 174, 176], "branches": [[170, 171], [170, 176], [171, 172], [171, 174]]}

import pytest
from ansible.vars.clean import namespace_facts

def module_response_deepcopy(value):
    # Mock implementation of module_response_deepcopy
    if isinstance(value, dict):
        return value.copy()
    return value

@pytest.fixture
def mock_module_response_deepcopy(monkeypatch):
    monkeypatch.setattr('ansible.vars.clean.module_response_deepcopy', module_response_deepcopy)

def test_namespace_facts_with_ansible_prefix(mock_module_response_deepcopy):
    facts = {
        'ansible_os_family': 'Debian',
        'ansible_distribution': 'Ubuntu',
        'ansible_local': 'local_value',
        'other_fact': 'value'
    }
    expected = {
        'ansible_facts': {
            'os_family': 'Debian',
            'distribution': 'Ubuntu',
            'ansible_local': 'local_value',
            'other_fact': 'value'
        }
    }
    result = namespace_facts(facts)
    assert result == expected

def test_namespace_facts_without_ansible_prefix(mock_module_response_deepcopy):
    facts = {
        'os_family': 'Debian',
        'distribution': 'Ubuntu',
        'other_fact': 'value'
    }
    expected = {
        'ansible_facts': {
            'os_family': 'Debian',
            'distribution': 'Ubuntu',
            'other_fact': 'value'
        }
    }
    result = namespace_facts(facts)
    assert result == expected

def test_namespace_facts_empty(mock_module_response_deepcopy):
    facts = {}
    expected = {'ansible_facts': {}}
    result = namespace_facts(facts)
    assert result == expected
