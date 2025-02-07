# file: lib/ansible/vars/manager.py:143-144
# asked: {"lines": [143, 144], "branches": []}
# gained: {"lines": [143, 144], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

def test_set_inventory():
    vm = VariableManager()
    inventory = "test_inventory"
    
    vm.set_inventory(inventory)
    
    assert vm._inventory == inventory
