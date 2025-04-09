# file lib/ansible/plugins/inventory/ini.py:102-136
# lines [104, 106, 108, 110, 111, 113, 114, 115, 117, 120, 121, 123, 124, 125, 129, 132, 134, 135, 136]
# branches ['110->111', '110->113', '124->125', '124->134', '125->129', '125->132']

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule
from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader

# Mocking the BaseFileInventoryPlugin since it's not provided in the snippet
class BaseFileInventoryPlugin:
    def parse(self, inventory, loader, path):
        pass

# Assuming to_bytes and to_text are utility functions that need to be mocked
def to_bytes(data, errors=None):
    return data.encode()

def to_text(data, errors=None):
    return data.decode()

@pytest.fixture
def inventory():
    return InventoryData()

@pytest.fixture
def loader(mocker):
    loader = DataLoader()
    mocker.patch.object(loader, '_get_file_contents', return_value=(b"invalid utf8: \x80", False))
    return loader

@pytest.fixture
def ini_path(tmp_path):
    p = tmp_path / "test.ini"
    p.write_text(u"invalid utf8: \x80", encoding='utf-8', errors='surrogateescape')
    return str(p)

def test_parse_with_invalid_utf8(inventory, loader, ini_path, mocker):
    mocker.patch('ansible.plugins.inventory.ini.to_bytes', side_effect=to_bytes)
    mocker.patch('ansible.plugins.inventory.ini.to_text', side_effect=to_text)

    with pytest.raises(AnsibleParserError):
        inv_module = InventoryModule()
        inv_module.parse(inventory, loader, ini_path)

    # Assert that the loader's _get_file_contents method was called
    loader._get_file_contents.assert_called_once_with(ini_path)

    # No need to assert to_bytes and to_text as they are utility functions and not methods of a class
