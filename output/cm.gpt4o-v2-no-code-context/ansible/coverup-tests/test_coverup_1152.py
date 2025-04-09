# file: lib/ansible/plugins/inventory/ini.py:285-316
# asked: {"lines": [301, 302, 303, 304, 306, 309, 310, 311, 312, 313, 314, 316], "branches": [[310, 311], [310, 316], [311, 312], [311, 313]]}
# gained: {"lines": [301, 302, 303, 304, 306, 309, 310, 311, 312, 313, 314, 316], "branches": [[310, 311], [310, 316], [311, 312], [311, 313]]}

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleParserError, AnsibleError

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module._filename = 'testfile'
    module.lineno = 1
    return module

def test_parse_host_definition_valid_line(inventory_module):
    line = "alpha user=admin"
    hostnames, port, variables = inventory_module._parse_host_definition(line)
    assert hostnames == ['alpha']
    assert port is None
    assert variables == {'user': 'admin'}

def test_parse_host_definition_invalid_syntax(inventory_module):
    line = "alpha user=admin invalid_syntax"
    with pytest.raises(AnsibleError, match="Expected key=value host variable assignment, got: invalid_syntax"):
        inventory_module._parse_host_definition(line)

def test_parse_host_definition_value_error(mocker, inventory_module):
    line = "alpha user=admin"
    mocker.patch('ansible.plugins.inventory.ini.shlex_split', side_effect=ValueError("mocked error"))
    with pytest.raises(AnsibleError, match="Error parsing host definition 'alpha user=admin': mocked error"):
        inventory_module._parse_host_definition(line)

def test_parse_host_definition_expand_hostpattern(mocker, inventory_module):
    line = "alpha user=admin"
    mocker.patch.object(inventory_module, '_expand_hostpattern', return_value=(['alpha'], 22))
    hostnames, port, variables = inventory_module._parse_host_definition(line)
    assert hostnames == ['alpha']
    assert port == 22
    assert variables == {'user': 'admin'}
