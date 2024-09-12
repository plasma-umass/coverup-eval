# file: lib/ansible/plugins/inventory/generator.py:103-105
# asked: {"lines": [103, 104, 105], "branches": []}
# gained: {"lines": [103, 104, 105], "branches": []}

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader
from unittest.mock import MagicMock

@pytest.fixture
def inventory_module():
    loader = DataLoader()
    templar = Templar(loader=loader)
    inventory_module = InventoryModule()
    inventory_module.templar = templar
    return inventory_module

def test_template_with_variables(inventory_module, mocker):
    pattern = "{{ var1 }} and {{ var2 }}"
    variables = {"var1": "value1", "var2": "value2"}
    
    mock_do_template = mocker.patch.object(inventory_module.templar, 'do_template', return_value="value1 and value2")
    
    result = inventory_module.template(pattern, variables)
    
    assert result == "value1 and value2"
    mock_do_template.assert_called_once_with(pattern)
    assert inventory_module.templar.available_variables == variables
