# file lib/ansible/plugins/inventory/generator.py:92-101
# lines [94, 95, 96, 98, 99, 101]
# branches ['95->96', '95->101', '98->99', '98->101']

import os
import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.constants import YAML_FILENAME_EXTENSIONS

# Mocking the BaseInventoryPlugin to control the behavior of verify_file
class MockedBaseInventoryPlugin:
    def verify_file(self, path):
        return True

# Test function to cover lines 94-101
def test_verify_file_with_valid_extensions(mocker):
    # Mock the super() call to return our mocked base plugin
    mocker.patch('ansible.plugins.inventory.generator.super', return_value=MockedBaseInventoryPlugin())

    # Create an instance of the InventoryModule
    inventory_module = InventoryModule()

    # Test with a valid YAML extension
    for ext in YAML_FILENAME_EXTENSIONS:
        file_path = f'test_inventory{ext}'
        assert inventory_module.verify_file(file_path) is True

    # Test with a '.config' extension
    file_path = 'test_inventory.config'
    assert inventory_module.verify_file(file_path) is True

    # Test with no extension
    file_path = 'test_inventory'
    assert inventory_module.verify_file(file_path) is True

# Test function to cover lines 94-101 with an invalid extension
def test_verify_file_with_invalid_extension(mocker):
    # Mock the super() call to return our mocked base plugin
    mocker.patch('ansible.plugins.inventory.generator.super', return_value=MockedBaseInventoryPlugin())

    # Create an instance of the InventoryModule
    inventory_module = InventoryModule()

    # Test with an invalid extension
    file_path = 'test_inventory.invalid'
    assert inventory_module.verify_file(file_path) is False
