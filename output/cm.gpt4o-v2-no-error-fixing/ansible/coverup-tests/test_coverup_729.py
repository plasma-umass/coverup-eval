# file: lib/ansible/plugins/inventory/ini.py:102-136
# asked: {"lines": [104, 106, 108, 110, 111, 113, 114, 115, 117, 120, 121, 123, 124, 125, 129, 132, 134, 135, 136], "branches": [[110, 111], [110, 113], [124, 125], [124, 134], [125, 129], [125, 132]]}
# gained: {"lines": [104, 106, 108, 110, 111, 113, 114, 115, 117, 120, 134, 135, 136], "branches": [[110, 111], [110, 113]]}

import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_bytes

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_with_loader(inventory_module):
    inventory = MagicMock()
    loader = MagicMock()
    path = 'dummy_path'
    b_data = b'[group]\nhost1\n'
    
    loader._get_file_contents.return_value = (b_data, False)
    
    inventory_module.parse(inventory, loader, path)
    
    loader._get_file_contents.assert_called_once_with(path)
    assert inventory_module._filename == path

def test_parse_without_loader(inventory_module):
    inventory = MagicMock()
    loader = None
    path = 'dummy_path'
    b_data = b'[group]\nhost1\n'
    
    with patch('builtins.open', mock_open(read_data=b_data)) as mock_file:
        inventory_module.parse(inventory, loader, path)
    
    mock_file.assert_called_once_with(to_bytes(path, errors='surrogate_or_strict'), 'rb')
    assert inventory_module._filename == path

def test_parse_unicode_error(inventory_module):
    inventory = MagicMock()
    loader = MagicMock()
    path = 'dummy_path'
    b_data = b'[group]\nhost1\n\x80\x80'
    
    loader._get_file_contents.return_value = (b_data, False)
    
    with patch.object(inventory_module, '_parse') as mock_parse:
        inventory_module.parse(inventory, loader, path)
    
    mock_parse.assert_called_once()
    assert inventory_module._filename == path

def test_parse_raises_ansible_parser_error(inventory_module):
    inventory = MagicMock()
    loader = MagicMock()
    path = 'dummy_path'
    
    loader._get_file_contents.side_effect = Exception('Test exception')
    
    with pytest.raises(AnsibleParserError, match='Test exception'):
        inventory_module.parse(inventory, loader, path)
