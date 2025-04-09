# file: lib/ansible/vars/manager.py:143-144
# asked: {"lines": [143, 144], "branches": []}
# gained: {"lines": [143, 144], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_set_inventory(variable_manager):
    inventory = "test_inventory"
    variable_manager.set_inventory(inventory)
    assert variable_manager._inventory == inventory
