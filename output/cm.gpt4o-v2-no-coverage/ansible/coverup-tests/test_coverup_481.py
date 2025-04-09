# file: lib/ansible/plugins/inventory/generator.py:92-101
# asked: {"lines": [92, 94, 95, 96, 98, 99, 101], "branches": [[95, 96], [95, 101], [98, 99], [98, 101]]}
# gained: {"lines": [92], "branches": []}

import os
import pytest
from ansible import constants as C
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.inventory.generator import InventoryModule

class MockBaseInventoryPlugin(BaseInventoryPlugin):
    def verify_file(self, path):
        return True

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, 'verify_file', MockBaseInventoryPlugin().verify_file)
    return module

def test_verify_file_with_valid_extension(inventory_module):
    valid_extensions = ['.config'] + C.YAML_FILENAME_EXTENSIONS
    for ext in valid_extensions:
        path = f"test{ext}"
        assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module, monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, 'verify_file', lambda path: False)
    path = "test.invalid"
    assert module.verify_file(path) == False

def test_verify_file_with_no_extension(inventory_module):
    path = "test"
    assert inventory_module.verify_file(path) == True
