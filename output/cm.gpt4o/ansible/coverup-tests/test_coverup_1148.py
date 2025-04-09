# file lib/ansible/plugins/inventory/generator.py:92-101
# lines [94, 95, 96, 98, 99, 101]
# branches ['95->96', '95->101', '98->99', '98->101']

import pytest
import os
from ansible.plugins.inventory.generator import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible import constants as C

class MockBaseInventoryPlugin(BaseInventoryPlugin):
    def verify_file(self, path):
        return True

@pytest.fixture
def mock_base_inventory_plugin(monkeypatch):
    monkeypatch.setattr(BaseInventoryPlugin, 'verify_file', MockBaseInventoryPlugin().verify_file)

def test_verify_file_valid_extension(mock_base_inventory_plugin):
    inventory = InventoryModule()
    valid_extensions = ['.config'] + C.YAML_FILENAME_EXTENSIONS
    for ext in valid_extensions:
        path = f"test{ext}"
        assert inventory.verify_file(path) is True

def test_verify_file_invalid_extension(mock_base_inventory_plugin):
    inventory = InventoryModule()
    path = "test.invalid"
    assert inventory.verify_file(path) is False
