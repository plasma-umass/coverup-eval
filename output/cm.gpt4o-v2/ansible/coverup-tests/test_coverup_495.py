# file: lib/ansible/vars/manager.py:684-695
# asked: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}
# gained: {"lines": [684, 689, 690, 692, 693, 694, 695], "branches": [[689, 690], [689, 692]]}

import pytest
from collections.abc import Mapping
from ansible.errors import AnsibleAssertionError
from ansible.vars.manager import VariableManager

class MockMapping(Mapping):
    def __init__(self, **kwargs):
        self._data = kwargs

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def update(self, other):
        self._data.update(other)

def test_set_nonpersistent_facts_with_valid_mapping():
    vm = VariableManager()
    vm._nonpersistent_fact_cache = {}
    host = 'localhost'
    facts = MockMapping(foo='bar')

    vm.set_nonpersistent_facts(host, facts)
    assert vm._nonpersistent_fact_cache[host] == facts

def test_set_nonpersistent_facts_with_invalid_mapping():
    vm = VariableManager()
    host = 'localhost'
    facts = ['not', 'a', 'mapping']

    with pytest.raises(AnsibleAssertionError) as excinfo:
        vm.set_nonpersistent_facts(host, facts)
    assert "the type of 'facts' to set for nonpersistent_facts should be a Mapping" in str(excinfo.value)

def test_set_nonpersistent_facts_updates_existing_facts():
    vm = VariableManager()
    host = 'localhost'
    vm._nonpersistent_fact_cache = {host: MockMapping(foo='bar')}
    new_facts = MockMapping(baz='qux')

    vm.set_nonpersistent_facts(host, new_facts)
    assert vm._nonpersistent_fact_cache[host]['foo'] == 'bar'
    assert vm._nonpersistent_fact_cache[host]['baz'] == 'qux'
