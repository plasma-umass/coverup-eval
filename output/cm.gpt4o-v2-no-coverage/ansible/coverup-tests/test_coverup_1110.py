# file: lib/ansible/plugins/inventory/ini.py:102-136
# asked: {"lines": [104, 106, 108, 110, 111, 113, 114, 115, 117, 120, 121, 123, 124, 125, 129, 132, 134, 135, 136], "branches": [[110, 111], [110, 113], [124, 125], [124, 134], [125, 129], [125, 132]]}
# gained: {"lines": [104, 106, 108, 110, 111, 113, 114, 115, 117, 120, 134, 135, 136], "branches": [[110, 111], [110, 113]]}

import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_bytes, to_text

class MockLoader:
    def _get_file_contents(self, path):
        return (b"mocked file contents", False)
    
    def get_basedir(self):
        return "mocked_basedir"

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_with_loader(inventory_module):
    inventory = MagicMock()
    loader = MockLoader()
    path = "mocked_path"

    with patch.object(inventory_module, '_parse', return_value=None):
        inventory_module.parse(inventory, loader, path)

    assert inventory_module._filename == path

@patch("builtins.open", new_callable=mock_open, read_data="mocked file contents")
def test_parse_without_loader(mock_file, inventory_module):
    inventory = MagicMock()
    loader = None
    path = "mocked_path"

    with patch.object(inventory_module, '_parse', return_value=None):
        inventory_module.parse(inventory, loader, path)

    assert inventory_module._filename == path
    mock_file.assert_called_once_with(to_bytes(path, errors='surrogate_or_strict'), 'rb')

def test_parse_unicode_error(inventory_module):
    inventory = MagicMock()
    loader = MockLoader()
    path = "mocked_path"

    with patch("ansible.module_utils._text.to_text", side_effect=UnicodeError):
        inventory_module.b_COMMENT_MARKERS = ['#']
        with patch.object(inventory_module, '_parse', return_value=None):
            inventory_module.parse(inventory, loader, path)

    assert inventory_module._filename == path

def test_parse_raises_ansible_parser_error(inventory_module):
    inventory = MagicMock()
    loader = MockLoader()
    path = "mocked_path"

    with patch.object(inventory_module, "_parse", side_effect=Exception("mocked exception")):
        with pytest.raises(AnsibleParserError, match="mocked exception"):
            inventory_module.parse(inventory, loader, path)
