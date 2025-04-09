# file: lib/ansible/plugins/inventory/yaml.py:171-177
# asked: {"lines": [171, 175, 177], "branches": []}
# gained: {"lines": [171, 175, 177], "branches": []}

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

class MockBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def _expand_hostpattern(self, host_pattern):
        return ['host1', 'host2'], 22

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, '_expand_hostpattern', MockBaseFileInventoryPlugin()._expand_hostpattern)
    return module

def test_parse_host(inventory_module):
    host_pattern = 'some_pattern'
    hostnames, port = inventory_module._parse_host(host_pattern)
    
    assert hostnames == ['host1', 'host2']
    assert port == 22
