# file: lib/ansible/plugins/inventory/toml.py:249-254
# asked: {"lines": [250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253], [252, 254]]}
# gained: {"lines": [250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253], [252, 254]]}

import os
import pytest
from ansible.plugins.inventory import BaseFileInventoryPlugin
from ansible.plugins.inventory.toml import InventoryModule

class MockBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def verify_file(self, path):
        return True

@pytest.fixture
def mock_base_file_inventory_plugin(monkeypatch):
    monkeypatch.setattr(BaseFileInventoryPlugin, 'verify_file', MockBaseFileInventoryPlugin().verify_file)

def test_verify_file_toml_extension(mock_base_file_inventory_plugin):
    inventory = InventoryModule()
    assert inventory.verify_file('test.toml') == True

def test_verify_file_non_toml_extension(mock_base_file_inventory_plugin):
    inventory = InventoryModule()
    assert inventory.verify_file('test.txt') == False

def test_verify_file_super_returns_false(monkeypatch):
    class MockBaseFileInventoryPluginFalse(BaseFileInventoryPlugin):
        def verify_file(self, path):
            return False

    monkeypatch.setattr(BaseFileInventoryPlugin, 'verify_file', MockBaseFileInventoryPluginFalse().verify_file)
    inventory = InventoryModule()
    assert inventory.verify_file('test.toml') == False
