# file: lib/ansible/vars/manager.py:110-123
# asked: {"lines": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 123], "branches": []}
# gained: {"lines": [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 123], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_getstate(variable_manager):
    state = variable_manager.__getstate__()
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
