# file: lib/ansible/plugins/inventory/yaml.py:171-177
# asked: {"lines": [171, 175, 177], "branches": []}
# gained: {"lines": [171, 175, 177], "branches": []}

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

class MockInventoryModule(InventoryModule):
    def _expand_hostpattern(self, hostpattern):
        if hostpattern == "valid_host":
            return (["host1", "host2"], 22)
        elif hostpattern == "invalid_host":
            return (["invalid_host"], None)
        else:
            return ([hostpattern], None)

@pytest.fixture
def inventory_module():
    return MockInventoryModule()

def test_parse_valid_host(inventory_module):
    hostnames, port = inventory_module._parse_host("valid_host")
    assert hostnames == ["host1", "host2"]
    assert port == 22

def test_parse_invalid_host(inventory_module):
    hostnames, port = inventory_module._parse_host("invalid_host")
    assert hostnames == ["invalid_host"]
    assert port is None

def test_parse_empty_host(inventory_module):
    hostnames, port = inventory_module._parse_host("")
    assert hostnames == [""]
    assert port is None
