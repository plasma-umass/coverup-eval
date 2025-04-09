# file: lib/ansible/vars/hostvars.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from ansible.vars.hostvars import HostVars
from ansible.module_utils.common._collections_compat import Mapping

class MockInventory:
    pass

class MockVariableManager:
    pass

class MockLoader:
    pass

@pytest.fixture
def hostvars():
    inventory = MockInventory()
    variable_manager = MockVariableManager()
    loader = MockLoader()
    return HostVars(inventory, variable_manager, loader)

def test_set_inventory(hostvars):
    new_inventory = MockInventory()
    hostvars.set_inventory(new_inventory)
    assert hostvars._inventory is new_inventory
