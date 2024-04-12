# file lib/ansible/vars/hostvars.py:51-55
# lines [51, 52, 53, 54, 55]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import MagicMock

# Assuming the existence of the HostVars class in the ansible.vars.hostvars module
# and that the Inventory and VariableManager classes are available for import.

@pytest.fixture
def inventory():
    return MagicMock()

@pytest.fixture
def variable_manager():
    return MagicMock()

@pytest.fixture
def loader():
    return MagicMock()

def test_hostvars_initialization(inventory, variable_manager, loader):
    hostvars = HostVars(inventory, variable_manager, loader)
    assert hostvars._inventory is inventory
    assert hostvars._loader is loader
    assert hostvars._variable_manager is variable_manager
    assert variable_manager._hostvars is hostvars

    # Cleanup (though in this case, it's not strictly necessary since we're using mocks)
    del hostvars._variable_manager._hostvars
