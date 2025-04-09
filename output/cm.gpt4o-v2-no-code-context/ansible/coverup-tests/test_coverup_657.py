# file: lib/ansible/vars/manager.py:139-141
# asked: {"lines": [139, 140, 141], "branches": []}
# gained: {"lines": [139, 140, 141], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    vm = VariableManager()
    vm._extra_vars = {'key': 'value'}
    return vm

def test_extra_vars_property(variable_manager):
    assert variable_manager.extra_vars == {'key': 'value'}
