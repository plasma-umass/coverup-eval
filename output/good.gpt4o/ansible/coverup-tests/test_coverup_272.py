# file lib/ansible/plugins/inventory/ini.py:318-334
# lines [318, 324, 326, 327, 328, 329, 331, 332, 334]
# branches ['326->327', '326->329', '329->331', '329->334', '331->329', '331->332']

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule

class MockBaseFileInventoryPlugin:
    def _expand_hostpattern(self, hostpattern):
        return (['localhost'], None)

@pytest.fixture
def inventory_module(mocker):
    mocker.patch('ansible.plugins.inventory.ini.BaseFileInventoryPlugin', MockBaseFileInventoryPlugin)
    return InventoryModule()

def test_expand_hostpattern_ends_with_colon(inventory_module):
    with pytest.raises(AnsibleParserError, match="Invalid host pattern 'localhost:' supplied, ending in ':' is not allowed, this character is reserved to provide a port."):
        inventory_module._expand_hostpattern('localhost:')

def test_expand_hostpattern_yaml_pattern(inventory_module):
    with pytest.raises(AnsibleParserError, match="Invalid host pattern '---' supplied, '---' is normally a sign this is a YAML file."):
        inventory_module._expand_hostpattern('---')

def test_expand_hostpattern_valid(inventory_module):
    hostnames, port = inventory_module._expand_hostpattern('localhost')
    assert hostnames == ['localhost']
    assert port is None
