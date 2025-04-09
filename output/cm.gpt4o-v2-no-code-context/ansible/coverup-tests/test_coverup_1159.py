# file: lib/ansible/plugins/inventory/ini.py:318-334
# asked: {"lines": [324, 326, 327, 328, 329, 331, 332, 334], "branches": [[326, 327], [326, 329], [329, 331], [329, 334], [331, 329], [331, 332]]}
# gained: {"lines": [324, 326, 327, 328, 329, 331, 332, 334], "branches": [[326, 327], [326, 329], [329, 331], [329, 334], [331, 329], [331, 332]]}

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleParserError

class MockBaseFileInventoryPlugin:
    def _expand_hostpattern(self, hostpattern):
        if hostpattern == 'host:':
            return (['host'], None)
        elif hostpattern == '---':
            return (['---'], None)
        return (['host1'], None)

@pytest.fixture
def inventory_module(monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.ini.BaseFileInventoryPlugin', MockBaseFileInventoryPlugin)
    return InventoryModule()

def test_expand_hostpattern_with_colon(inventory_module):
    with pytest.raises(AnsibleParserError, match="Invalid host pattern 'host:' supplied, ending in ':' is not allowed, this character is reserved to provide a port."):
        inventory_module._expand_hostpattern('host:')

def test_expand_hostpattern_with_yaml_pattern(monkeypatch, inventory_module):
    with pytest.raises(AnsibleParserError, match="Invalid host pattern '---' supplied, '---' is normally a sign this is a YAML file."):
        inventory_module._expand_hostpattern('---')

def test_expand_hostpattern_valid(inventory_module):
    hostnames, port = inventory_module._expand_hostpattern('host1')
    assert hostnames == ['host1']
    assert port is None
