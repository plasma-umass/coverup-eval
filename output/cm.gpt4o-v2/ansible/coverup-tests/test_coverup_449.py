# file: lib/ansible/vars/manager.py:697-706
# asked: {"lines": [697, 701, 702, 703, 704, 706], "branches": [[701, 702], [701, 703], [703, 704], [703, 706]]}
# gained: {"lines": [697, 701, 702, 703, 704, 706], "branches": [[701, 702], [701, 703], [703, 704], [703, 706]]}

import pytest
from unittest.mock import MagicMock
from ansible.vars.manager import VariableManager
from ansible.module_utils.common._collections_compat import MutableMapping

class MockMutableMapping(dict, MutableMapping):
    pass

@pytest.fixture
def variable_manager():
    vm = VariableManager()
    vm._vars_cache = {}
    return vm

def test_set_host_variable_new_host(variable_manager):
    host = 'host1'
    varname = 'var1'
    value = 'value1'
    
    variable_manager.set_host_variable(host, varname, value)
    
    assert host in variable_manager._vars_cache
    assert variable_manager._vars_cache[host][varname] == value

def test_set_host_variable_existing_host_new_var(variable_manager):
    host = 'host1'
    varname = 'var1'
    value = 'value1'
    variable_manager._vars_cache[host] = {}
    
    variable_manager.set_host_variable(host, varname, value)
    
    assert variable_manager._vars_cache[host][varname] == value

def test_set_host_variable_existing_host_existing_var_non_mapping(variable_manager):
    host = 'host1'
    varname = 'var1'
    value = 'value1'
    variable_manager._vars_cache[host] = {varname: 'old_value'}
    
    variable_manager.set_host_variable(host, varname, value)
    
    assert variable_manager._vars_cache[host][varname] == value

def test_set_host_variable_existing_host_existing_var_mapping(variable_manager, monkeypatch):
    host = 'host1'
    varname = 'var1'
    old_value = MockMutableMapping({'key1': 'old_value1'})
    new_value = MockMutableMapping({'key2': 'new_value2'})
    combined_value = {'key1': 'old_value1', 'key2': 'new_value2'}
    
    variable_manager._vars_cache[host] = {varname: old_value}
    
    def mock_combine_vars(a, b):
        return combined_value
    
    monkeypatch.setattr('ansible.vars.manager.combine_vars', mock_combine_vars)
    
    variable_manager.set_host_variable(host, varname, new_value)
    
    assert variable_manager._vars_cache[host] == combined_value
