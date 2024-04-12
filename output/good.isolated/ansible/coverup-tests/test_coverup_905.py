# file lib/ansible/plugins/inventory/generator.py:88-90
# lines [88, 90]
# branches []

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin

# Mocking the BaseInventoryPlugin to avoid side effects
class MockedBaseInventoryPlugin(BaseInventoryPlugin):
    def __init__(self):
        pass  # Override the __init__ to prevent any side effects

# Applying the mock using pytest-mock
def test_inventory_module_initialization(mocker):
    mocker.patch('ansible.plugins.inventory.generator.BaseInventoryPlugin', new=MockedBaseInventoryPlugin)
    
    # Create an instance of InventoryModule, which should now use the mocked BaseInventoryPlugin
    inventory_module = InventoryModule()
    
    # Assertions to verify postconditions (none in this case, as __init__ has no return value or side effects)
    assert isinstance(inventory_module, InventoryModule)
