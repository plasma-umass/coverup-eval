# file lib/ansible/vars/manager.py:684-695
# lines [689, 690, 692, 693, 694, 695]
# branches ['689->690', '689->692']

import pytest
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleAssertionError
from collections.abc import Mapping

class TestVariableManager:
    
    def test_set_nonpersistent_facts_invalid_type(self):
        vm = VariableManager()
        host = 'localhost'
        facts = ['not', 'a', 'mapping']
        
        with pytest.raises(AnsibleAssertionError) as excinfo:
            vm.set_nonpersistent_facts(host, facts)
        
        assert "the type of 'facts' to set for nonpersistent_facts should be a Mapping but is a" in str(excinfo.value)
    
    def test_set_nonpersistent_facts_key_error(self, mocker):
        vm = VariableManager()
        host = 'localhost'
        facts = {'key': 'value'}
        
        # Mock the _nonpersistent_fact_cache to simulate KeyError
        mocker.patch.object(vm, '_nonpersistent_fact_cache', {})
        
        vm.set_nonpersistent_facts(host, facts)
        
        assert vm._nonpersistent_fact_cache[host] == facts
    
    def test_set_nonpersistent_facts_update(self, mocker):
        vm = VariableManager()
        host = 'localhost'
        initial_facts = {'key1': 'value1'}
        new_facts = {'key2': 'value2'}
        
        # Mock the _nonpersistent_fact_cache to have initial facts
        mocker.patch.object(vm, '_nonpersistent_fact_cache', {host: initial_facts})
        
        vm.set_nonpersistent_facts(host, new_facts)
        
        expected_facts = {'key1': 'value1', 'key2': 'value2'}
        assert vm._nonpersistent_fact_cache[host] == expected_facts
