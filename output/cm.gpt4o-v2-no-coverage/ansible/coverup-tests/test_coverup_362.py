# file: lib/ansible/vars/manager.py:110-123
# asked: {"lines": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 123], "branches": []}
# gained: {"lines": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 123], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    manager = VariableManager()
    manager._fact_cache = MagicMock()
    manager._nonpersistent_fact_cache = MagicMock()
    manager._vars_cache = MagicMock()
    manager._extra_vars = MagicMock()
    manager._host_vars_files = MagicMock()
    manager._group_vars_files = MagicMock()
    manager._omit_token = MagicMock()
    manager._options_vars = MagicMock()
    manager._inventory = MagicMock()
    manager.safe_basedir = MagicMock()
    return manager

def test_getstate(variable_manager):
    state = variable_manager.__getstate__()
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
