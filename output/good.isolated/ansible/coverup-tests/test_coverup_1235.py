# file lib/ansible/vars/manager.py:110-123
# lines [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 123]
# branches []

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    # Setup code to create a VariableManager instance
    vm = VariableManager()
    # Mocking internal attributes to simulate a state
    vm._fact_cache = {}
    vm._nonpersistent_fact_cache = {}
    vm._vars_cache = {}
    vm._extra_vars = {}
    vm._host_vars_files = {}
    vm._group_vars_files = {}
    vm._omit_token = None
    vm._options_vars = {}
    vm._inventory = None
    vm.safe_basedir = None
    yield vm
    # Teardown code if necessary

def test_variable_manager_getstate(variable_manager):
    # Call __getstate__ to trigger the code in question
    state = variable_manager.__getstate__()

    # Assertions to verify the state contains the correct keys and values
    assert 'fact_cache' in state
    assert 'np_fact_cache' in state
    assert 'vars_cache' in state
    assert 'extra_vars' in state
    assert 'host_vars_files' in state
    assert 'group_vars_files' in state
    assert 'omit_token' in state
    assert 'options_vars' in state
    assert 'inventory' in state
    assert 'safe_basedir' in state

    # Verify that the values match the expected mocked values
    assert state['fact_cache'] == variable_manager._fact_cache
    assert state['np_fact_cache'] == variable_manager._nonpersistent_fact_cache
    assert state['vars_cache'] == variable_manager._vars_cache
    assert state['extra_vars'] == variable_manager._extra_vars
    assert state['host_vars_files'] == variable_manager._host_vars_files
    assert state['group_vars_files'] == variable_manager._group_vars_files
    assert state['omit_token'] == variable_manager._omit_token
    assert state['options_vars'] == variable_manager._options_vars
    assert state['inventory'] == variable_manager._inventory
    assert state['safe_basedir'] == variable_manager.safe_basedir
