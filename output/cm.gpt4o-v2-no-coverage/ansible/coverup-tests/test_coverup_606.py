# file: lib/ansible/plugins/inventory/ini.py:268-283
# asked: {"lines": [268, 279, 280, 281, 283], "branches": [[279, 280], [279, 283]]}
# gained: {"lines": [268, 279, 280, 281, 283], "branches": [[279, 280], [279, 283]]}

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleError

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module._filename = "testfile.ini"
    module.lineno = 1
    return module

def test_parse_variable_definition_valid(inventory_module, mocker):
    mocker.patch.object(inventory_module, '_parse_value', return_value='parsed_value')
    line = "key=value"
    key, value = inventory_module._parse_variable_definition(line)
    assert key == "key"
    assert value == "parsed_value"

def test_parse_variable_definition_invalid(inventory_module):
    line = "invalid_line"
    with pytest.raises(AnsibleError, match="testfile.ini:1: Expected key=value, got: invalid_line"):
        inventory_module._parse_variable_definition(line)
