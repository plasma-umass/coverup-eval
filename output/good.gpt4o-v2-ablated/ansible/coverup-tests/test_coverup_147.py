# file: lib/ansible/plugins/inventory/yaml.py:87-94
# asked: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[90, 91], [90, 94], [92, 93], [92, 94]]}
# gained: {"lines": [87, 89, 90, 91, 92, 93, 94], "branches": [[90, 91], [92, 93], [92, 94]]}

import os
import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

class MockBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def verify_file(self, path):
        return True

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, 'get_option', lambda x: ['.yaml', '.yml'])
    return module

def test_verify_file_with_valid_extension(inventory_module, tmp_path):
    test_file = tmp_path / "test.yaml"
    test_file.write_text("content")
    assert inventory_module.verify_file(str(test_file)) is True

def test_verify_file_with_invalid_extension(inventory_module, tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert inventory_module.verify_file(str(test_file)) is False

def test_verify_file_with_no_extension(inventory_module, tmp_path):
    test_file = tmp_path / "testfile"
    test_file.write_text("content")
    assert inventory_module.verify_file(str(test_file)) is True

def test_verify_file_super_returns_false(monkeypatch, tmp_path):
    class MockInventoryModule(InventoryModule):
        def verify_file(self, path):
            return False

    module = MockInventoryModule()
    monkeypatch.setattr(module, 'get_option', lambda x: ['.yaml', '.yml'])
    test_file = tmp_path / "test.yaml"
    test_file.write_text("content")
    assert module.verify_file(str(test_file)) is False
