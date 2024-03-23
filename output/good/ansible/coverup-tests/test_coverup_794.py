# file lib/ansible/module_utils/facts/compat.py:37-46
# lines [37, 45, 46]
# branches []

import pytest
from ansible.module_utils.facts.compat import get_all_facts
from ansible.module_utils.basic import AnsibleModule

# Mock the ansible_facts function
def mock_ansible_facts(module, gather_subset):
    # Return a mock fact dictionary based on the gather_subset
    return {'mock_fact': 'mock_value'} if 'all' in gather_subset else {}

@pytest.fixture
def mock_module(mocker):
    # Create a mock AnsibleModule with a 'gather_subset' parameter
    mock_module = mocker.MagicMock(spec=AnsibleModule)
    mock_module.params = {'gather_subset': ['all']}
    return mock_module

@pytest.fixture
def mock_ansible_facts_function(mocker):
    # Patch the ansible_facts function with our mock
    mocker.patch('ansible.module_utils.facts.compat.ansible_facts', side_effect=mock_ansible_facts)

def test_get_all_facts_with_gather_subset_all(mock_module, mock_ansible_facts_function):
    # Call get_all_facts with a mock module that has 'gather_subset' set to ['all']
    facts = get_all_facts(mock_module)
    
    # Assert that the returned facts contain our mock fact
    assert 'mock_fact' in facts
    assert facts['mock_fact'] == 'mock_value'

def test_get_all_facts_with_gather_subset_not_all(mock_module, mock_ansible_facts_function):
    # Modify the mock_module to have a different 'gather_subset'
    mock_module.params['gather_subset'] = ['network']
    
    # Call get_all_facts with the modified mock module
    facts = get_all_facts(mock_module)
    
    # Assert that the returned facts do not contain our mock fact
    assert 'mock_fact' not in facts
