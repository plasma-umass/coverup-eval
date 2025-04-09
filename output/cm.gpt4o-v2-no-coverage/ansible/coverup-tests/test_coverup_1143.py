# file: lib/ansible/plugins/inventory/generator.py:92-101
# asked: {"lines": [94, 95, 96, 98, 99, 101], "branches": [[95, 96], [95, 101], [98, 99], [98, 101]]}
# gained: {"lines": [94, 95, 96, 98, 99, 101], "branches": [[95, 96], [98, 99], [98, 101]]}

import os
import pytest
from ansible import constants as C
from ansible.plugins.inventory.generator import InventoryModule

class MockBaseInventoryPlugin:
    def verify_file(self, path):
        return True

@pytest.fixture
def inventory_module(monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.generator.BaseInventoryPlugin.verify_file', MockBaseInventoryPlugin().verify_file)
    return InventoryModule()

def test_verify_file_with_valid_extension(inventory_module):
    valid_extensions = ['.config'] + C.YAML_FILENAME_EXTENSIONS
    for ext in valid_extensions:
        path = f"test{ext}"
        assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module):
    path = "test.invalid"
    assert inventory_module.verify_file(path) == False

def test_verify_file_with_no_extension(inventory_module):
    path = "test"
    assert inventory_module.verify_file(path) == True
