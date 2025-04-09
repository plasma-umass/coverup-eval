# file: lib/ansible/plugins/inventory/ini.py:285-316
# asked: {"lines": [285, 301, 302, 303, 304, 306, 309, 310, 311, 312, 313, 314, 316], "branches": [[310, 311], [310, 316], [311, 312], [311, 313]]}
# gained: {"lines": [285, 301, 302, 303, 304, 306, 309, 310, 311, 312, 313, 314, 316], "branches": [[310, 311], [310, 316], [311, 312], [311, 313]]}

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleError, AnsibleParserError

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module._filename = "testfile"
    module.lineno = 1
    return module

def test_parse_host_definition_valid_line(inventory_module):
    line = "beta:2345 user=admin"
    hostnames, port, variables = inventory_module._parse_host_definition(line)
    assert hostnames == ["beta"]
    assert port == 2345
    assert variables == {"user": "admin"}

def test_parse_host_definition_invalid_line(inventory_module):
    line = "invalid line without equals"
    with pytest.raises(AnsibleError, match="Expected key=value host variable assignment, got: line"):
        inventory_module._parse_host_definition(line)

def test_parse_host_definition_invalid_syntax(inventory_module, mocker):
    line = "beta:2345 user=admin"
    mocker.patch('ansible.plugins.inventory.ini.shlex_split', side_effect=ValueError("Invalid syntax"))
    with pytest.raises(AnsibleError, match="Error parsing host definition 'beta:2345 user=admin': Invalid syntax"):
        inventory_module._parse_host_definition(line)

def test_parse_host_definition_expand_hostpattern_error(inventory_module, mocker):
    line = "beta: user=admin"
    mocker.patch.object(inventory_module, '_expand_hostpattern', side_effect=AnsibleParserError("Invalid host pattern"))
    with pytest.raises(AnsibleParserError, match="Invalid host pattern"):
        inventory_module._parse_host_definition(line)

def test_parse_host_definition_parse_value(inventory_module, mocker):
    line = "beta:2345 user=admin"
    mock_parse_value = mocker.patch.object(inventory_module, '_parse_value', return_value="parsed_value")
    hostnames, port, variables = inventory_module._parse_host_definition(line)
    assert variables["user"] == "parsed_value"
    mock_parse_value.assert_called_once_with("admin")
