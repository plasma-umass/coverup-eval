# file lib/ansible/plugins/inventory/yaml.py:83-85
# lines [83, 85]
# branches []

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

# Mock context to prevent side effects
@pytest.fixture
def ansible_context(mocker):
    mocker.patch.object(InventoryManager, '__init__', return_value=None)
    mocker.patch.object(VariableManager, '__init__', return_value=None)
    mocker.patch.object(DataLoader, '__init__', return_value=None)

def test_inventory_module_initialization(ansible_context):
    # Instantiate the InventoryModule
    inventory_module = InventoryModule()

    # Assertions to ensure the object is created and is an instance of InventoryModule
    assert inventory_module is not None
    assert isinstance(inventory_module, InventoryModule)

    # Clean up
    del inventory_module
