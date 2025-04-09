# file: lib/ansible/plugins/inventory/generator.py:103-105
# asked: {"lines": [103, 104, 105], "branches": []}
# gained: {"lines": [103, 104, 105], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.inventory.generator import InventoryModule

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.templar = MagicMock()
    return module

def test_template(inventory_module):
    pattern = "Hello, {{ name }}!"
    variables = {"name": "World"}
    
    inventory_module.templar.do_template.return_value = "Hello, World!"
    
    result = inventory_module.template(pattern, variables)
    
    inventory_module.templar.available_variables = variables
    inventory_module.templar.do_template.assert_called_once_with(pattern)
    
    assert result == "Hello, World!"
