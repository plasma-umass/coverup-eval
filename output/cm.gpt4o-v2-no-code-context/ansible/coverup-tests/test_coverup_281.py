# file: lib/ansible/vars/manager.py:110-123
# asked: {"lines": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 123], "branches": []}
# gained: {"lines": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 123], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    vm = VariableManager()
    vm._fact_cache = {'host1': {'fact1': 'value1'}}
    vm._nonpersistent_fact_cache = {'host2': {'fact2': 'value2'}}
    vm._vars_cache = {'host3': {'var1': 'value3'}}
    vm._extra_vars = {'extra_var1': 'extra_value1'}
    vm._host_vars_files = ['host_vars_file1']
    vm._group_vars_files = ['group_vars_file1']
    vm._omit_token = 'omit_token_value'
    vm._options_vars = {'option_var1': 'option_value1'}
    vm._inventory = 'inventory_value'
    vm.safe_basedir = 'safe_basedir_value'
    return vm

def test_getstate(variable_manager):
    state = variable_manager.__getstate__()
    assert state['fact_cache'] == {'host1': {'fact1': 'value1'}}
    assert state['np_fact_cache'] == {'host2': {'fact2': 'value2'}}
    assert state['vars_cache'] == {'host3': {'var1': 'value3'}}
    assert state['extra_vars'] == {'extra_var1': 'extra_value1'}
    assert state['host_vars_files'] == ['host_vars_file1']
    assert state['group_vars_files'] == ['group_vars_file1']
    assert state['omit_token'] == 'omit_token_value'
    assert state['options_vars'] == {'option_var1': 'option_value1'}
    assert state['inventory'] == 'inventory_value'
    assert state['safe_basedir'] == 'safe_basedir_value'
