# file: lib/ansible/vars/manager.py:684-695
# asked: {"lines": [689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}
# gained: {"lines": [689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}

import pytest
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleAssertionError
from collections.abc import Mapping

class TestVariableManager:
    @pytest.fixture
    def variable_manager(self):
        vm = VariableManager()
        vm._nonpersistent_fact_cache = {}
        return vm

    def test_set_nonpersistent_facts_with_valid_mapping(self, variable_manager):
        host = 'localhost'
        facts = {'fact1': 'value1', 'fact2': 'value2'}
        
        variable_manager.set_nonpersistent_facts(host, facts)
        
        assert variable_manager._nonpersistent_fact_cache[host] == facts

    def test_set_nonpersistent_facts_with_invalid_mapping(self, variable_manager):
        host = 'localhost'
        facts = ['not', 'a', 'mapping']
        
        with pytest.raises(AnsibleAssertionError) as excinfo:
            variable_manager.set_nonpersistent_facts(host, facts)
        
        assert "the type of 'facts' to set for nonpersistent_facts should be a Mapping" in str(excinfo.value)

    def test_set_nonpersistent_facts_update_existing(self, variable_manager):
        host = 'localhost'
        initial_facts = {'fact1': 'value1'}
        new_facts = {'fact2': 'value2'}
        
        variable_manager._nonpersistent_fact_cache[host] = initial_facts
        variable_manager.set_nonpersistent_facts(host, new_facts)
        
        expected_facts = {'fact1': 'value1', 'fact2': 'value2'}
        assert variable_manager._nonpersistent_fact_cache[host] == expected_facts
