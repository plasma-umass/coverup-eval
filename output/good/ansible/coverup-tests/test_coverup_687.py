# file lib/ansible/plugins/inventory/ini.py:95-100
# lines [95, 97, 99, 100]
# branches []

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleError

# Assuming the existence of a BaseFileInventoryPlugin mock
class MockBaseFileInventoryPlugin:
    def __init__(self):
        pass

@pytest.fixture
def inventory_module(mocker):
    mocker.patch('ansible.plugins.inventory.ini.BaseFileInventoryPlugin', new=MockBaseFileInventoryPlugin)
    return InventoryModule()

def test_inventory_module_initialization(inventory_module):
    assert isinstance(inventory_module, InventoryModule)
    assert inventory_module.patterns == {}
    assert inventory_module._filename is None
