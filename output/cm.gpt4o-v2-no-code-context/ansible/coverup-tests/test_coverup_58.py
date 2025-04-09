# file: lib/ansible/plugins/inventory/advanced_host_list.py:31-63
# asked: {"lines": [31, 33, 35, 37, 38, 39, 40, 41, 43, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63], "branches": [[39, 40], [39, 41], [49, 0], [49, 50], [51, 49], [51, 52], [59, 49], [59, 60], [60, 59], [60, 61]]}
# gained: {"lines": [31, 33, 35, 37, 38, 39, 40, 41, 43, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63], "branches": [[39, 40], [39, 41], [49, 0], [49, 50], [51, 52], [59, 49], [59, 60], [60, 59], [60, 61]]}

import pytest
from ansible.plugins.inventory.advanced_host_list import InventoryModule
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.utils.display import Display
import os
from unittest.mock import patch, MagicMock

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def inventory():
    loader = DataLoader()
    return InventoryManager(loader=loader)

def test_verify_file_with_comma(inventory_module):
    host_list = "host1,host2"
    assert inventory_module.verify_file(host_list) == True

def test_verify_file_without_comma(inventory_module, monkeypatch):
    host_list = "host1"
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    assert inventory_module.verify_file(host_list) == False

def test_parse_valid_host_list(inventory_module, inventory, monkeypatch):
    host_list = "host1,host2"
    inventory_module.inventory = inventory
    inventory_module.display = Display()
    
    with patch.object(inventory_module, '_expand_hostpattern', return_value=(["host1", "host2"], None)):
        inventory_module.parse(inventory, None, host_list)
    
    assert "host1" in inventory.hosts
    assert "host2" in inventory.hosts

def test_parse_invalid_host_list(inventory_module, inventory, monkeypatch):
    host_list = "host1,host2"
    inventory_module.inventory = inventory
    inventory_module.display = Display()
    
    with patch.object(inventory_module, '_expand_hostpattern', side_effect=AnsibleError("error")):
        inventory_module.parse(inventory, None, host_list)
    
    assert "host1" in inventory.hosts
    assert "host2" in inventory.hosts

def test_parse_raises_ansible_parser_error(inventory_module, inventory, monkeypatch):
    host_list = "host1,host2"
    inventory_module.inventory = inventory
    inventory_module.display = Display()
    
    with patch.object(inventory_module, '_expand_hostpattern', side_effect=Exception("error")):
        with pytest.raises(AnsibleParserError, match="Invalid data from string, could not parse: error"):
            inventory_module.parse(inventory, None, host_list)
