# file lib/ansible/vars/manager.py:143-144
# lines [143, 144]
# branches []

import pytest
from ansible.vars.manager import VariableManager

@pytest.fixture
def mock_inventory():
    class MockInventory:
        pass
    return MockInventory()

def test_set_inventory(mock_inventory):
    var_manager = VariableManager()
    var_manager.set_inventory(mock_inventory)
    assert var_manager._inventory is mock_inventory
