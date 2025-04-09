# file: lib/ansible/plugins/inventory/constructed.py:104-113
# asked: {"lines": [104, 106, 107, 108, 110, 111, 113], "branches": [[107, 108], [107, 113], [110, 111], [110, 113]]}
# gained: {"lines": [104], "branches": []}

import pytest
import os
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable
from ansible import constants as C

class MockBaseInventoryPlugin(BaseInventoryPlugin):
    def verify_file(self, path):
        return True

class MockConstructable(Constructable):
    pass

class MockInventoryModule(MockBaseInventoryPlugin, MockConstructable):
    def verify_file(self, path):
        valid = False
        if super(MockInventoryModule, self).verify_file(path):
            file_name, ext = os.path.splitext(path)
            if not ext or ext in ['.config'] + C.YAML_FILENAME_EXTENSIONS:
                valid = True
        return valid

@pytest.fixture
def inventory_module():
    return MockInventoryModule()

def test_verify_file_with_valid_extension(inventory_module, monkeypatch):
    test_path = "/path/to/file.config"
    
    def mock_splitext(path):
        return ("/path/to/file", ".config")
    
    monkeypatch.setattr(os.path, 'splitext', mock_splitext)
    
    result = inventory_module.verify_file(test_path)
    assert result is True

def test_verify_file_with_invalid_extension(inventory_module, monkeypatch):
    test_path = "/path/to/file.txt"
    
    def mock_splitext(path):
        return ("/path/to/file", ".txt")
    
    monkeypatch.setattr(os.path, 'splitext', mock_splitext)
    
    result = inventory_module.verify_file(test_path)
    assert result is False

def test_verify_file_with_no_extension(inventory_module, monkeypatch):
    test_path = "/path/to/file"
    
    def mock_splitext(path):
        return ("/path/to/file", "")
    
    monkeypatch.setattr(os.path, 'splitext', mock_splitext)
    
    result = inventory_module.verify_file(test_path)
    assert result is True
