# file lib/ansible/plugins/inventory/constructed.py:98-102
# lines [98, 100, 102]
# branches []

import pytest
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.inventory.data import InventoryData
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleError

# Mock classes to avoid side effects
class MockFactCache(dict):
    def __init__(self, *args, **kwargs):
        super(MockFactCache, self).__init__(*args, **kwargs)

    def get(self, item, default=None):
        return self.get(item, default)

    def set(self, item, value):
        self[item] = value

@pytest.fixture
def inventory_module(mocker):
    mocker.patch('ansible.plugins.inventory.constructed.FactCache', MockFactCache)
    inventory = InventoryModule()
    inventory._inventory = InventoryData()
    inventory._templar = Templar(loader=DataLoader())
    inventory._variable_manager = VariableManager()
    return inventory

def test_inventory_module_initialization(inventory_module):
    assert isinstance(inventory_module._cache, MockFactCache), "InventoryModule cache should be an instance of MockFactCache"
