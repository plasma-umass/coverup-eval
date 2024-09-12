# file: lib/ansible/plugins/inventory/yaml.py:171-177
# asked: {"lines": [171, 175, 177], "branches": []}
# gained: {"lines": [171, 175, 177], "branches": []}

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

class MockBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def _expand_hostpattern(self, host_pattern):
        if host_pattern == "valid_pattern":
            return (["host1", "host2"], 22)
        elif host_pattern == "empty_pattern":
            return ([], None)
        else:
            raise ValueError("Invalid host pattern")

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, '_expand_hostpattern', MockBaseFileInventoryPlugin()._expand_hostpattern)
    return module

def test_parse_host_valid_pattern(inventory_module):
    hostnames, port = inventory_module._parse_host("valid_pattern")
    assert hostnames == ["host1", "host2"]
    assert port == 22

def test_parse_host_empty_pattern(inventory_module):
    hostnames, port = inventory_module._parse_host("empty_pattern")
    assert hostnames == []
    assert port is None

def test_parse_host_invalid_pattern(inventory_module):
    with pytest.raises(ValueError, match="Invalid host pattern"):
        inventory_module._parse_host("invalid_pattern")
