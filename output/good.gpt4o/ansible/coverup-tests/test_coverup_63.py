# file lib/ansible/plugins/inventory/advanced_host_list.py:31-63
# lines [31, 33, 35, 37, 38, 39, 40, 41, 43, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63]
# branches ['39->40', '39->41', '49->exit', '49->50', '51->49', '51->52', '59->49', '59->60', '60->59', '60->61']

import pytest
from ansible.plugins.inventory.advanced_host_list import InventoryModule
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch
import os

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_inventory():
    inventory = MagicMock()
    inventory.hosts = {}
    return inventory

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_display():
    display = Display()
    return display

def test_verify_file_with_comma(inventory_module):
    host_list = "host1,host2"
    assert inventory_module.verify_file(host_list) == True

def test_verify_file_without_comma(inventory_module):
    host_list = "host1"
    assert inventory_module.verify_file(host_list) == False

def test_parse_valid_host_list(inventory_module, mock_inventory, mock_loader, mock_display):
    host_list = "host1,host2"
    inventory_module.inventory = mock_inventory
    inventory_module.display = mock_display

    with patch.object(inventory_module, '_expand_hostpattern', return_value=(["host1", "host2"], None)):
        inventory_module.parse(mock_inventory, mock_loader, host_list)
        assert "host1" in mock_inventory.add_host.call_args_list[0][0]
        assert "host2" in mock_inventory.add_host.call_args_list[1][0]

def test_parse_invalid_host_list(inventory_module, mock_inventory, mock_loader, mock_display):
    host_list = "host1,host2"
    inventory_module.inventory = mock_inventory
    inventory_module.display = mock_display

    with patch.object(inventory_module, '_expand_hostpattern', side_effect=AnsibleError("error")):
        inventory_module.parse(mock_inventory, mock_loader, host_list)
        assert "host1" in mock_inventory.add_host.call_args_list[0][0]
        assert "host2" in mock_inventory.add_host.call_args_list[1][0]

def test_parse_raises_ansible_parser_error(inventory_module, mock_inventory, mock_loader, mock_display):
    host_list = "host1,host2"
    inventory_module.inventory = mock_inventory
    inventory_module.display = mock_display

    with patch.object(inventory_module, '_expand_hostpattern', side_effect=Exception("error")):
        with pytest.raises(AnsibleParserError, match="Invalid data from string, could not parse: error"):
            inventory_module.parse(mock_inventory, mock_loader, host_list)
