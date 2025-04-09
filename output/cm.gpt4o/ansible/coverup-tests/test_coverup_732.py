# file lib/ansible/module_utils/facts/compat.py:37-46
# lines [37, 45, 46]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the function get_all_facts is imported from ansible.module_utils.facts.compat
from ansible.module_utils.facts.compat import get_all_facts

def test_get_all_facts(mocker):
    # Mock the AnsibleModule and its params
    mock_module = Mock()
    mock_module.params = {'gather_subset': ['all']}
    
    # Mock the ansible_facts function
    mock_ansible_facts = mocker.patch('ansible.module_utils.facts.compat.ansible_facts', return_value={'default_ipv4': '192.168.1.1'})
    
    # Call the function
    result = get_all_facts(mock_module)
    
    # Assertions to verify the function behavior
    mock_ansible_facts.assert_called_once_with(mock_module, gather_subset=['all'])
    assert result == {'default_ipv4': '192.168.1.1'}
