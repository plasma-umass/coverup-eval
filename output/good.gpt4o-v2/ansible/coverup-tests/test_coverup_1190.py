# file: lib/ansible/plugins/inventory/generator.py:92-101
# asked: {"lines": [94, 95, 96, 98, 99, 101], "branches": [[95, 96], [95, 101], [98, 99], [98, 101]]}
# gained: {"lines": [94, 95, 96, 98, 99, 101], "branches": [[95, 96], [98, 99], [98, 101]]}

import os
import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible import constants as C

class MockBaseInventoryPlugin(BaseInventoryPlugin):
    def verify_file(self, path):
        return True

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(BaseInventoryPlugin, 'verify_file', MockBaseInventoryPlugin().verify_file)
    return module

def test_verify_file_with_config_extension(inventory_module):
    path = "/path/to/file.config"
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_yaml_extension(inventory_module):
    for ext in C.YAML_FILENAME_EXTENSIONS:
        path = f"/path/to/file{ext}"
        assert inventory_module.verify_file(path) == True

def test_verify_file_with_no_extension(inventory_module):
    path = "/path/to/file"
    assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module):
    path = "/path/to/file.txt"
    assert inventory_module.verify_file(path) == False
