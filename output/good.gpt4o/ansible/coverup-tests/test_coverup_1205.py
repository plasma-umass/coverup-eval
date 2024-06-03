# file lib/ansible/plugins/inventory/ini.py:268-283
# lines [279, 280, 281, 283]
# branches ['279->280', '279->283']

import pytest
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_variable_definition_valid(inventory_module):
    line = "key=value"
    key, value = inventory_module._parse_variable_definition(line)
    assert key == "key"
    assert value == "value"

def test_parse_variable_definition_invalid(mocker, inventory_module):
    line = "invalid_line"
    mocker.patch.object(inventory_module, '_raise_error', side_effect=Exception("Expected key=value, got: invalid_line"))
    with pytest.raises(Exception) as excinfo:
        inventory_module._parse_variable_definition(line)
    assert "Expected key=value, got: invalid_line" in str(excinfo.value)
