# file lib/ansible/vars/manager.py:697-706
# lines [701, 702, 703, 704, 706]
# branches ['701->702', '701->703', '703->704', '703->706']

import pytest
from unittest.mock import MagicMock
from collections.abc import MutableMapping
from ansible.vars.manager import VariableManager

class TestVariableManager:
    @pytest.fixture
    def variable_manager(self):
        vm = VariableManager()
        vm._vars_cache = {}
        return vm

    def test_set_host_variable_new_host(self, variable_manager):
        host = 'test_host'
        varname = 'test_var'
        value = 'test_value'
        
        variable_manager.set_host_variable(host, varname, value)
        
        assert host in variable_manager._vars_cache
        assert variable_manager._vars_cache[host][varname] == value

    def test_set_host_variable_existing_host_new_var(self, variable_manager):
        host = 'test_host'
        varname = 'test_var'
        value = 'test_value'
        
        variable_manager._vars_cache[host] = {}
        variable_manager.set_host_variable(host, varname, value)
        
        assert variable_manager._vars_cache[host][varname] == value

    def test_set_host_variable_existing_var_combining(self, variable_manager, mocker):
        host = 'test_host'
        varname = 'test_var'
        existing_value = {'key1': 'value1'}
        new_value = {'key2': 'value2'}
        
        variable_manager._vars_cache[host] = {varname: existing_value}
        
        mocker.patch('ansible.vars.manager.combine_vars', return_value={varname: {**existing_value, **new_value}})
        
        variable_manager.set_host_variable(host, varname, new_value)
        
        assert variable_manager._vars_cache[host][varname] == {**existing_value, **new_value}

    def test_set_host_variable_existing_var_non_combining(self, variable_manager):
        host = 'test_host'
        varname = 'test_var'
        existing_value = 'old_value'
        new_value = 'new_value'
        
        variable_manager._vars_cache[host] = {varname: existing_value}
        
        variable_manager.set_host_variable(host, varname, new_value)
        
        assert variable_manager._vars_cache[host][varname] == new_value
