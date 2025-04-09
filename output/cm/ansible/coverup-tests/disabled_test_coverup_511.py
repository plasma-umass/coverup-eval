# file lib/ansible/vars/manager.py:684-695
# lines [684, 689, 690, 692, 693, 694, 695]
# branches ['689->690', '689->692']

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.vars.manager import VariableManager
from collections.abc import Mapping

class MockMapping(Mapping):
    def __init__(self, *args, **kwargs):
        self._storage = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self._storage[key]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)

    def update(self, other):
        self._storage.update(other)

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_set_nonpersistent_facts_with_valid_mapping(variable_manager):
    host = 'testhost'
    facts = MockMapping({'key': 'value'})
    variable_manager._nonpersistent_fact_cache = {}
    variable_manager.set_nonpersistent_facts(host, facts)
    assert variable_manager._nonpersistent_fact_cache[host] == facts._storage

def test_set_nonpersistent_facts_with_update_existing_host(variable_manager):
    host = 'testhost'
    initial_facts = MockMapping({'key': 'value'})
    new_facts = MockMapping({'new_key': 'new_value'})
    variable_manager._nonpersistent_fact_cache = {host: initial_facts}
    variable_manager.set_nonpersistent_facts(host, new_facts)
    assert variable_manager._nonpersistent_fact_cache[host] == {'key': 'value', 'new_key': 'new_value'}

def test_set_nonpersistent_facts_with_invalid_facts_type(variable_manager):
    host = 'testhost'
    facts = ['not', 'a', 'mapping']
    variable_manager._nonpersistent_fact_cache = {}
    with pytest.raises(AnsibleAssertionError):
        variable_manager.set_nonpersistent_facts(host, facts)
