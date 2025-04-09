# file: lib/ansible/vars/manager.py:684-695
# asked: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}
# gained: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}

import pytest
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleAssertionError
from collections.abc import Mapping

class TestVariableManager:
    
    @pytest.fixture
    def variable_manager(self):
        return VariableManager()

    def test_set_nonpersistent_facts_with_invalid_facts(self, variable_manager):
        host = 'localhost'
        facts = ['not', 'a', 'mapping']
        
        with pytest.raises(AnsibleAssertionError) as excinfo:
            variable_manager.set_nonpersistent_facts(host, facts)
        
        assert "the type of 'facts' to set for nonpersistent_facts should be a Mapping but is a" in str(excinfo.value)

    def test_set_nonpersistent_facts_with_new_host(self, variable_manager):
        host = 'localhost'
        facts = {'key': 'value'}
        
        variable_manager._nonpersistent_fact_cache = {}
        variable_manager.set_nonpersistent_facts(host, facts)
        
        assert variable_manager._nonpersistent_fact_cache[host] == facts

    def test_set_nonpersistent_facts_with_existing_host(self, variable_manager):
        host = 'localhost'
        initial_facts = {'key1': 'value1'}
        new_facts = {'key2': 'value2'}
        
        variable_manager._nonpersistent_fact_cache = {host: initial_facts}
        variable_manager.set_nonpersistent_facts(host, new_facts)
        
        expected_facts = {'key1': 'value1', 'key2': 'value2'}
        assert variable_manager._nonpersistent_fact_cache[host] == expected_facts
