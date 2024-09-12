# file: lib/ansible/vars/hostvars.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import MagicMock

@pytest.fixture
def hostvars():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    return HostVars(inventory, variable_manager, loader)

def test_set_inventory(hostvars):
    new_inventory = MagicMock()
    hostvars.set_inventory(new_inventory)
    assert hostvars._inventory == new_inventory
