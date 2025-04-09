# file lib/ansible/plugins/inventory/ini.py:285-316
# lines [285, 301, 302, 303, 304, 306, 309, 310, 311, 312, 313, 314, 316]
# branches ['310->311', '310->316', '311->312', '311->313']

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleParserError
from unittest.mock import MagicMock

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module._raise_error = MagicMock(side_effect=AnsibleParserError)
    module._expand_hostpattern = MagicMock(return_value=(['hostname'], None))
    module._parse_value = MagicMock(return_value='parsed_value')
    return module

def test_parse_host_definition_with_invalid_token(inventory_module):
    invalid_line = "hostname invalid_token"
    with pytest.raises(AnsibleParserError):
        inventory_module._parse_host_definition(invalid_line)
    inventory_module._raise_error.assert_called_once_with("Expected key=value host variable assignment, got: invalid_token")

def test_parse_host_definition_with_shlex_error(inventory_module, mocker):
    mocker.patch('ansible.plugins.inventory.ini.shlex_split', side_effect=ValueError("shlex error"))
    with pytest.raises(AnsibleParserError):
        inventory_module._parse_host_definition("hostname user=admin")
    inventory_module._raise_error.assert_called_once_with("Error parsing host definition 'hostname user=admin': shlex error")
