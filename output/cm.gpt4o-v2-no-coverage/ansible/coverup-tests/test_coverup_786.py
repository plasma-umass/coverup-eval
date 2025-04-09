# file: lib/ansible/plugins/inventory/yaml.py:171-177
# asked: {"lines": [171, 175, 177], "branches": []}
# gained: {"lines": [171, 175, 177], "branches": []}

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

class MockBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def _expand_hostpattern(self, hostpattern):
        if hostpattern == "host1":
            return (["host1"], None)
        elif hostpattern == "host2:22":
            return (["host2"], 22)
        else:
            return (["unknown"], None)

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, "_expand_hostpattern", MockBaseFileInventoryPlugin()._expand_hostpattern)
    return module

def test_parse_host_single_host(inventory_module):
    hostnames, port = inventory_module._parse_host("host1")
    assert hostnames == ["host1"]
    assert port is None

def test_parse_host_with_port(inventory_module):
    hostnames, port = inventory_module._parse_host("host2:22")
    assert hostnames == ["host2"]
    assert port == 22

def test_parse_host_unknown(inventory_module):
    hostnames, port = inventory_module._parse_host("unknown")
    assert hostnames == ["unknown"]
    assert port is None
