# file lib/ansible/vars/manager.py:661-682
# lines [666, 667, 669, 670, 671, 673, 675, 676, 677, 679, 682]
# branches ['666->667', '666->669', '675->676', '675->679']

import pytest
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleAssertionError
from collections.abc import Mapping, MutableMapping

class MockFactCache(MutableMapping):
    def __init__(self, *args, **kwargs):
        self.store = dict()
    def __getitem__(self, key):
        return self.store[key]
    def __setitem__(self, key, value):
        self.store[key] = value
    def __delitem__(self, key):
        del self.store[key]
    def __iter__(self):
        return iter(self.store)
    def __len__(self):
        return len(self.store)

@pytest.fixture
def variable_manager(mocker):
    vm = VariableManager()
    mocker.patch.object(vm, '_fact_cache', new_callable=MockFactCache)
    return vm

def test_set_host_facts_with_non_mapping_facts(variable_manager):
    with pytest.raises(AnsibleAssertionError):
        variable_manager.set_host_facts('host1', 'not_a_mapping')

def test_set_host_facts_with_new_host(variable_manager):
    facts = {'key': 'value'}
    variable_manager.set_host_facts('host1', facts)
    assert variable_manager._fact_cache['host1'] == facts

def test_set_host_facts_with_existing_host_and_non_mutable_mapping(variable_manager):
    variable_manager._fact_cache['host1'] = 'not_a_mutable_mapping'
    with pytest.raises(TypeError):
        variable_manager.set_host_facts('host1', {'key': 'value'})

def test_set_host_facts_with_existing_host_and_mutable_mapping(variable_manager):
    variable_manager._fact_cache['host1'] = {'original_key': 'original_value'}
    new_facts = {'new_key': 'new_value'}
    variable_manager.set_host_facts('host1', new_facts)
    assert variable_manager._fact_cache['host1'] == {'original_key': 'original_value', 'new_key': 'new_value'}
