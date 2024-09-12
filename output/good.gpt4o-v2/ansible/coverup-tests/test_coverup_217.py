# file: lib/ansible/vars/manager.py:661-682
# asked: {"lines": [661, 666, 667, 669, 670, 671, 673, 675, 676, 677, 679, 682], "branches": [[666, 667], [666, 669], [675, 676], [675, 679]]}
# gained: {"lines": [661, 666, 667, 669, 670, 671, 673, 675, 676, 677, 679, 682], "branches": [[666, 667], [666, 669], [675, 676], [675, 679]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.module_utils.common._collections_compat import Mapping, MutableMapping
from ansible.vars.manager import VariableManager

class TestVariableManager:
    
    @pytest.fixture
    def variable_manager(self):
        vm = VariableManager()
        vm._fact_cache = {}
        return vm

    def test_set_host_facts_with_invalid_facts_type(self, variable_manager):
        with pytest.raises(AnsibleAssertionError):
            variable_manager.set_host_facts('host1', ['not', 'a', 'mapping'])

    def test_set_host_facts_with_new_host(self, variable_manager):
        facts = {'key': 'value'}
        variable_manager.set_host_facts('host1', facts)
        assert variable_manager._fact_cache['host1'] == facts

    def test_set_host_facts_with_existing_host_and_invalid_cache_type(self, variable_manager):
        variable_manager._fact_cache['host1'] = ['not', 'a', 'mutablemapping']
        with pytest.raises(TypeError):
            variable_manager.set_host_facts('host1', {'key': 'value'})

    def test_set_host_facts_with_existing_host_and_valid_cache(self, variable_manager):
        variable_manager._fact_cache['host1'] = {'existing_key': 'existing_value'}
        new_facts = {'new_key': 'new_value'}
        variable_manager.set_host_facts('host1', new_facts)
        assert variable_manager._fact_cache['host1'] == {'existing_key': 'existing_value', 'new_key': 'new_value'}
