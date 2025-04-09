# file: lib/ansible/module_utils/facts/compat.py:37-46
# asked: {"lines": [37, 45, 46], "branches": []}
# gained: {"lines": [37, 45, 46], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming ansible_facts and AnsibleModule are imported from their respective modules

def test_get_all_facts(monkeypatch):
    # Mocking the AnsibleModule and its params
    mock_module = Mock()
    mock_module.params = {'gather_subset': ['all']}
    
    # Mocking the ansible_facts function
    def mock_ansible_facts(module, gather_subset=None):
        assert module == mock_module
        assert gather_subset == ['all']
        return {'default_ipv4': '192.168.1.1'}
    
    monkeypatch.setattr('ansible.module_utils.facts.compat.ansible_facts', mock_ansible_facts)
    
    from ansible.module_utils.facts.compat import get_all_facts
    
    result = get_all_facts(mock_module)
    
    assert result == {'default_ipv4': '192.168.1.1'}
