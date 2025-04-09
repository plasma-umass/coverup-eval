# file: lib/ansible/module_utils/facts/compat.py:37-46
# asked: {"lines": [37, 45, 46], "branches": []}
# gained: {"lines": [37, 45, 46], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming ansible_facts is a function that needs to be imported
from ansible.module_utils.facts.compat import get_all_facts
from ansible.module_utils.facts import ansible_facts

@pytest.fixture
def mock_module():
    module = Mock()
    module.params = {'gather_subset': ['all']}
    return module

def test_get_all_facts(mock_module, mocker):
    # Mock ansible_facts to avoid calling the actual function
    mock_ansible_facts = mocker.patch('ansible.module_utils.facts.compat.ansible_facts', return_value={'default_ipv4': '192.168.1.1'})
    
    result = get_all_facts(mock_module)
    
    # Verify that ansible_facts was called with the correct parameters
    mock_ansible_facts.assert_called_once_with(mock_module, gather_subset=['all'])
    
    # Verify the result
    assert result == {'default_ipv4': '192.168.1.1'}
