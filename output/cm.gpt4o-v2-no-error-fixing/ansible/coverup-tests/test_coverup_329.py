# file: lib/ansible/vars/manager.py:684-695
# asked: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}
# gained: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.module_utils.common._collections_compat import Mapping
from ansible.vars.manager import VariableManager

class TestVariableManager:
    
    @pytest.fixture
    def variable_manager(self):
        vm = VariableManager()
        vm._nonpersistent_fact_cache = {}
        return vm

    def test_set_nonpersistent_facts_with_mapping(self, variable_manager):
        host = 'localhost'
        facts = {'key': 'value'}
        
        variable_manager.set_nonpersistent_facts(host, facts)
        
        assert variable_manager._nonpersistent_fact_cache[host] == facts

    def test_set_nonpersistent_facts_with_non_mapping(self, variable_manager):
        host = 'localhost'
        facts = ['not', 'a', 'mapping']
        
        with pytest.raises(AnsibleAssertionError, match="the type of 'facts' to set for nonpersistent_facts should be a Mapping but is a <class 'list'>"):
            variable_manager.set_nonpersistent_facts(host, facts)

    def test_set_nonpersistent_facts_updates_existing(self, variable_manager):
        host = 'localhost'
        initial_facts = {'key1': 'value1'}
        new_facts = {'key2': 'value2'}
        
        variable_manager.set_nonpersistent_facts(host, initial_facts)
        variable_manager.set_nonpersistent_facts(host, new_facts)
        
        expected_facts = {'key1': 'value1', 'key2': 'value2'}
        assert variable_manager._nonpersistent_fact_cache[host] == expected_facts
