# file lib/ansible/plugins/inventory/ini.py:285-316
# lines [285, 301, 302, 303, 304, 306, 309, 310, 311, 312, 313, 314, 316]
# branches ['310->311', '310->316', '311->312', '311->313']

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleParserError, AnsibleError

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module._filename = 'testfile.ini'
    module.lineno = 1
    return module

def test_parse_host_definition_valid_line(inventory_module):
    line = "alpha:22 user=admin"
    hostnames, port, variables = inventory_module._parse_host_definition(line)
    
    assert hostnames == ['alpha']
    assert port == 22
    assert variables == {'user': 'admin'}

def test_parse_host_definition_invalid_line(inventory_module):
    line = "alpha:22 user=admin invalid_token"
    
    with pytest.raises(AnsibleError) as excinfo:
        inventory_module._parse_host_definition(line)
    
    assert "Expected key=value host variable assignment" in str(excinfo.value)

def test_parse_host_definition_shlex_error(mocker, inventory_module):
    line = "alpha:22 user=admin"
    mocker.patch('ansible.plugins.inventory.ini.shlex_split', side_effect=ValueError("mocked error"))
    
    with pytest.raises(AnsibleError) as excinfo:
        inventory_module._parse_host_definition(line)
    
    assert "Error parsing host definition" in str(excinfo.value)
