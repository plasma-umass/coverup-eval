# file lib/ansible/vars/manager.py:697-706
# lines [701, 702, 703, 704, 706]
# branches ['701->702', '701->703', '703->704', '703->706']

import pytest
from collections.abc import MutableMapping
from ansible.vars.manager import VariableManager
from ansible.utils.vars import combine_vars

class MockHost:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def variable_manager():
    # Assuming VariableManager has an __init__ that initializes _vars_cache
    vm = VariableManager()
    vm._vars_cache = {}
    return vm

@pytest.fixture
def mock_host():
    return MockHost(name='test_host')

def test_set_host_variable_with_mutable_mapping(variable_manager, mock_host, mocker):
    mocker.patch('ansible.vars.manager.combine_vars', side_effect=combine_vars)
    
    varname = 'test_var'
    initial_value = {'key1': 'value1'}
    new_value = {'key2': 'value2'}
    
    # Set initial variable
    variable_manager.set_host_variable(mock_host, varname, initial_value)
    assert variable_manager._vars_cache.get(mock_host) == {varname: initial_value}
    
    # Set new variable with MutableMapping
    variable_manager.set_host_variable(mock_host, varname, new_value)
    assert varname in variable_manager._vars_cache[mock_host]
    assert isinstance(variable_manager._vars_cache[mock_host][varname], MutableMapping)
    combined_value = combine_vars(variable_manager._vars_cache[mock_host], {varname: new_value})
    assert variable_manager._vars_cache[mock_host][varname] == combined_value[varname]
    
    # Cleanup
    del variable_manager._vars_cache[mock_host]
