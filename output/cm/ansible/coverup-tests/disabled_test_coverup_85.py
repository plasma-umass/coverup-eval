# file lib/ansible/plugins/inventory/host_list.py:35-66
# lines [35, 37, 39, 41, 42, 43, 44, 45, 47, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66]
# branches ['43->44', '43->45', '53->exit', '53->54', '55->53', '55->56', '63->53', '63->64']

import os
import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory.host_list import InventoryModule
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

# Mock the BaseInventoryPlugin since it's not provided in the snippet
class BaseInventoryPlugin:
    def parse(self, inventory, loader, path, cache=True):
        pass

# Mock the display object since it's not provided in the snippet
class DisplayMock:
    def vvv(self, msg):
        pass

# Include the InventoryModule class here with the mock base and display
class InventoryModule(InventoryModule):
    def __init__(self):
        self.display = DisplayMock()

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def inventory():
    return InventoryManager(loader=DataLoader())

def test_verify_file_with_nonexistent_path_and_comma(inventory_module):
    host_list = "nonexistent1,nonexistent2"
    assert inventory_module.verify_file(host_list) is True

def test_parse_with_invalid_host(inventory_module, inventory, mocker):
    mocker.patch('os.path.exists', return_value=False)
    host_list = "invalid_host,"
    # The test expects an AnsibleParserError, but the code does not raise it for invalid hosts.
    # The test should be modified to not expect an exception, and instead check for the host presence.
    inventory_module.parse(inventory, None, host_list)
    assert 'invalid_host' in inventory.hosts

def test_parse_with_valid_host(inventory_module, inventory, mocker):
    mocker.patch('os.path.exists', return_value=False)
    host_list = "localhost,"
    inventory_module.parse(inventory, None, host_list)
    assert 'localhost' in inventory.hosts

def test_parse_with_host_and_port(inventory_module, inventory, mocker):
    mocker.patch('os.path.exists', return_value=False)
    host_list = "localhost:8080,"
    inventory_module.parse(inventory, None, host_list)
    assert 'localhost' in inventory.hosts
    assert inventory.hosts['localhost'].vars['ansible_port'] == 8080

def test_parse_with_range_error(inventory_module, inventory, mocker):
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('ansible.plugins.inventory.host_list.parse_address', side_effect=AnsibleError("Invalid range"))
    host_list = "bad[range],"
    inventory_module.parse(inventory, None, host_list)
    assert 'bad[range]' in inventory.hosts

def test_parse_with_exception(inventory_module, inventory, mocker):
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('ansible.plugins.inventory.host_list.parse_address', side_effect=Exception("Generic exception"))
    host_list = "badhost,"
    with pytest.raises(AnsibleParserError):
        inventory_module.parse(inventory, None, host_list)
