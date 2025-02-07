# file: lib/ansible/plugins/inventory/constructed.py:104-113
# asked: {"lines": [106, 107, 108, 110, 111, 113], "branches": [[107, 108], [107, 113], [110, 111], [110, 113]]}
# gained: {"lines": [106, 107, 108, 110, 111, 113], "branches": [[107, 108], [107, 113], [110, 111], [110, 113]]}

import os
import pytest
from unittest.mock import patch
from ansible.plugins.inventory.constructed import InventoryModule
from ansible import constants as C

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_super_verify_file():
    with patch('ansible.plugins.inventory.constructed.BaseInventoryPlugin.verify_file') as mock_verify:
        yield mock_verify

def test_verify_file_with_valid_extension(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = True
    valid_extensions = ['.config'] + C.YAML_FILENAME_EXTENSIONS

    for ext in valid_extensions:
        path = f'/some/path/file{ext}'
        assert inventory_module.verify_file(path) == True

def test_verify_file_with_invalid_extension(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = True
    path = '/some/path/file.invalid'
    assert inventory_module.verify_file(path) == False

def test_verify_file_with_no_extension(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = True
    path = '/some/path/file'
    assert inventory_module.verify_file(path) == True

def test_verify_file_super_returns_false(inventory_module, mock_super_verify_file):
    mock_super_verify_file.return_value = False
    path = '/some/path/file.config'
    assert inventory_module.verify_file(path) == False
