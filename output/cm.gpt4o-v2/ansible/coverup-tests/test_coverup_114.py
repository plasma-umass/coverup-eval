# file: lib/ansible/plugins/inventory/toml.py:199-224
# asked: {"lines": [199, 200, 201, 203, 204, 205, 207, 208, 209, 210, 211, 212, 213, 215, 216, 217, 218, 220, 221, 222, 223], "branches": [[200, 201], [200, 203], [204, 205], [204, 207]]}
# gained: {"lines": [199, 200, 201, 203, 204, 205, 207, 208, 209, 210, 211, 212, 213, 215, 216, 217, 218, 220, 221, 222, 223], "branches": [[200, 201], [200, 203], [204, 205], [204, 207]]}

import pytest
from unittest.mock import Mock, patch, mock_open
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.module_utils.six import string_types
import toml
from ansible.plugins.inventory.toml import InventoryModule

class TestInventoryModule:

    @patch('ansible.plugins.inventory.toml.InventoryModule.parse')
    def test_load_file_invalid_filename(self, mock_parse):
        inventory = InventoryModule()
        inventory.loader = Mock()
        with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
            inventory._load_file(None)
        with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
            inventory._load_file(123)

    @patch('ansible.plugins.inventory.toml.InventoryModule.parse')
    def test_load_file_not_exists(self, mock_parse):
        inventory = InventoryModule()
        inventory.loader = Mock()
        inventory.loader.path_dwim.return_value = '/non/existent/path'
        inventory.loader.path_exists.return_value = False
        with pytest.raises(AnsibleFileNotFound, match="Unable to retrieve file contents"):
            inventory._load_file('non_existent_file.toml')

    @patch('ansible.plugins.inventory.toml.InventoryModule.parse')
    def test_load_file_toml_decode_error(self, mock_parse):
        inventory = InventoryModule()
        inventory.loader = Mock()
        inventory.loader.path_dwim.return_value = '/path/to/file'
        inventory.loader.path_exists.return_value = True
        inventory.loader._get_file_contents.return_value = (b'invalid_toml', False)
        with pytest.raises(AnsibleParserError, match=r"TOML file \(file\.toml\) is invalid: Key name found without value\. Reached end of file\. \(line 1 column 13 char 12\)"):
            inventory._load_file('file.toml')

    @patch('ansible.plugins.inventory.toml.InventoryModule.parse')
    def test_load_file_io_error(self, mock_parse):
        inventory = InventoryModule()
        inventory.loader = Mock()
        inventory.loader.path_dwim.return_value = '/path/to/file'
        inventory.loader.path_exists.return_value = True
        inventory.loader._get_file_contents.side_effect = IOError("IO error")
        with pytest.raises(AnsibleParserError, match="An error occurred while trying to read the file 'file.toml'"):
            inventory._load_file('file.toml')

    @patch('ansible.plugins.inventory.toml.InventoryModule.parse')
    def test_load_file_unexpected_error(self, mock_parse):
        inventory = InventoryModule()
        inventory.loader = Mock()
        inventory.loader.path_dwim.return_value = '/path/to/file'
        inventory.loader.path_exists.return_value = True
        inventory.loader._get_file_contents.side_effect = Exception("Unexpected error")
        with pytest.raises(AnsibleParserError, match="An unexpected error occurred while parsing the file 'file.toml'"):
            inventory._load_file('file.toml')

    @patch('ansible.plugins.inventory.toml.InventoryModule.parse')
    def test_load_file_success(self, mock_parse):
        inventory = InventoryModule()
        inventory.loader = Mock()
        inventory.loader.path_dwim.return_value = '/path/to/file'
        inventory.loader.path_exists.return_value = True
        inventory.loader._get_file_contents.return_value = (b'key = "value"', False)
        result = inventory._load_file('file.toml')
        assert result == {'key': 'value'}
