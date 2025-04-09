# file lib/ansible/vars/manager.py:661-682
# lines [666, 667, 669, 670, 671, 673, 675, 676, 677, 679, 682]
# branches ['666->667', '666->669', '675->676', '675->679']

import pytest
from unittest.mock import MagicMock
from collections.abc import Mapping, MutableMapping
from ansible.errors import AnsibleAssertionError
from ansible.vars.manager import VariableManager

class TestVariableManager:
    
    @pytest.fixture
    def variable_manager(self):
        vm = VariableManager()
        vm._fact_cache = {}
        return vm

    def test_set_host_facts_with_invalid_facts_type(self, variable_manager):
        with pytest.raises(AnsibleAssertionError, match="the type of 'facts' to set for host_facts should be a Mapping but is a"):
            variable_manager.set_host_facts('host1', ['not', 'a', 'mapping'])

    def test_set_host_facts_with_new_host(self, variable_manager):
        facts = {'key': 'value'}
        variable_manager.set_host_facts('host1', facts)
        assert variable_manager._fact_cache['host1'] == facts

    def test_set_host_facts_with_existing_host_invalid_cache_type(self, variable_manager):
        variable_manager._fact_cache['host1'] = ['not', 'a', 'mutable', 'mapping']
        facts = {'key': 'value'}
        with pytest.raises(TypeError, match='The object retrieved for host1 must be a MutableMapping but was'):
            variable_manager.set_host_facts('host1', facts)

    def test_set_host_facts_with_existing_host_valid_cache_type(self, variable_manager):
        variable_manager._fact_cache['host1'] = {'existing_key': 'existing_value'}
        facts = {'key': 'value'}
        variable_manager.set_host_facts('host1', facts)
        assert variable_manager._fact_cache['host1'] == {'existing_key': 'existing_value', 'key': 'value'}
