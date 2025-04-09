# file: lib/ansible/vars/manager.py:684-695
# asked: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}
# gained: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.module_utils.common._collections_compat import Mapping
from ansible.vars.manager import VariableManager

class TestVariableManager:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.vm = VariableManager()
        self.vm._nonpersistent_fact_cache = {}

    def test_set_nonpersistent_facts_with_mapping(self):
        host = 'localhost'
        facts = {'key': 'value'}
        
        self.vm.set_nonpersistent_facts(host, facts)
        
        assert self.vm._nonpersistent_fact_cache[host] == facts

    def test_set_nonpersistent_facts_with_non_mapping(self):
        host = 'localhost'
        facts = ['not', 'a', 'mapping']
        
        with pytest.raises(AnsibleAssertionError):
            self.vm.set_nonpersistent_facts(host, facts)

    def test_set_nonpersistent_facts_updates_existing_facts(self):
        host = 'localhost'
        initial_facts = {'key1': 'value1'}
        new_facts = {'key2': 'value2'}
        
        self.vm.set_nonpersistent_facts(host, initial_facts)
        self.vm.set_nonpersistent_facts(host, new_facts)
        
        expected_facts = {'key1': 'value1', 'key2': 'value2'}
        assert self.vm._nonpersistent_fact_cache[host] == expected_facts
