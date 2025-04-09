# file: lib/ansible/vars/manager.py:143-144
# asked: {"lines": [143, 144], "branches": []}
# gained: {"lines": [143, 144], "branches": []}

import pytest
from ansible.vars.manager import VariableManager
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_set_inventory(variable_manager):
    inventory = "test_inventory"
    variable_manager.set_inventory(inventory)
    assert variable_manager._inventory == inventory

def test_variable_manager_init():
    loader = "test_loader"
    inventory = "test_inventory"
    version_info = "test_version_info"
    vm = VariableManager(loader=loader, inventory=inventory, version_info=version_info)
    assert vm._inventory == inventory
    assert vm._loader == loader
    assert vm._hostvars is None
    assert vm._omit_token.startswith('__omit_place_holder__')
    assert isinstance(vm._fact_cache, (dict, FactCache))
