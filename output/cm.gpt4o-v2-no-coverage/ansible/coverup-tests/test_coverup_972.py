# file: lib/ansible/vars/hostvars.py:124-128
# asked: {"lines": [124, 128], "branches": []}
# gained: {"lines": [124, 128], "branches": []}

import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import MagicMock

@pytest.fixture
def hostvars():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    return HostVars(inventory, variable_manager, loader)

def test_deepcopy(hostvars):
    import copy
    memo = {}
    copied = copy.deepcopy(hostvars, memo)
    assert copied is hostvars

def test_hostvars_initialization():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    hostvars = HostVars(inventory, variable_manager, loader)
    
    assert hostvars._inventory is inventory
    assert hostvars._loader is loader
    assert hostvars._variable_manager is variable_manager
    assert variable_manager._hostvars is hostvars
