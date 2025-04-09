# file: lib/ansible/vars/manager.py:697-706
# asked: {"lines": [697, 701, 702, 703, 704, 706], "branches": [[701, 702], [701, 703], [703, 704], [703, 706]]}
# gained: {"lines": [697, 701, 702, 703, 704, 706], "branches": [[701, 702], [701, 703], [703, 704], [703, 706]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.utils.vars import combine_vars
from ansible.vars.manager import VariableManager

class TestVariableManager:
    @pytest.fixture
    def variable_manager(self):
        vm = VariableManager()
        vm._vars_cache = {}
        return vm

    def test_set_host_variable_new_host(self, variable_manager):
        host = 'host1'
        varname = 'var1'
        value = 'value1'
        
        variable_manager.set_host_variable(host, varname, value)
        
        assert host in variable_manager._vars_cache
        assert variable_manager._vars_cache[host][varname] == value

    def test_set_host_variable_existing_host_new_var(self, variable_manager):
        host = 'host1'
        varname = 'var1'
        value = 'value1'
        
        variable_manager._vars_cache[host] = {}
        variable_manager.set_host_variable(host, varname, value)
        
        assert variable_manager._vars_cache[host][varname] == value

    def test_set_host_variable_existing_host_existing_var_non_mapping(self, variable_manager):
        host = 'host1'
        varname = 'var1'
        value = 'value1'
        
        variable_manager._vars_cache[host] = {varname: 'old_value'}
        variable_manager.set_host_variable(host, varname, value)
        
        assert variable_manager._vars_cache[host][varname] == value

    def test_set_host_variable_existing_host_existing_var_mapping(self, variable_manager, monkeypatch):
        host = 'host1'
        varname = 'var1'
        value = {'key': 'value'}
        
        old_value = MagicMock(spec=MutableMapping)
        variable_manager._vars_cache[host] = {varname: old_value}
        
        def mock_combine_vars(a, b, merge=None):
            return {**a, **b}
        
        monkeypatch.setattr('ansible.utils.vars.combine_vars', mock_combine_vars)
        
        variable_manager.set_host_variable(host, varname, value)
        
        assert variable_manager._vars_cache[host] == {varname: value}
