# file lib/ansible/vars/manager.py:143-144
# lines [143, 144]
# branches []

import pytest
from ansible.vars.manager import VariableManager

class MockInventory:
    pass

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_set_inventory(variable_manager):
    mock_inventory = MockInventory()
    variable_manager.set_inventory(mock_inventory)
    assert variable_manager._inventory is mock_inventory, "The inventory was not set correctly"
