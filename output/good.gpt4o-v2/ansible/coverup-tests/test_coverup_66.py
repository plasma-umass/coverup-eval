# file: lib/ansible/plugins/inventory/advanced_host_list.py:31-63
# asked: {"lines": [31, 33, 35, 37, 38, 39, 40, 41, 43, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63], "branches": [[39, 40], [39, 41], [49, 0], [49, 50], [51, 49], [51, 52], [59, 49], [59, 60], [60, 59], [60, 61]]}
# gained: {"lines": [31, 33, 35, 37, 38, 39, 40, 41, 43, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63], "branches": [[39, 40], [39, 41], [49, 0], [49, 50], [51, 52], [59, 49], [59, 60], [60, 61]]}

import os
import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.inventory.advanced_host_list import InventoryModule

class MockInventory:
    def __init__(self):
        self.hosts = {}

    def add_host(self, host, group, port):
        self.hosts[host] = {'group': group, 'port': port}

class MockLoader:
    def get_basedir(self):
        return './'

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_verify_file_with_comma(inventory_module):
    host_list = "host1,host2"
    assert inventory_module.verify_file(host_list) == True

def test_verify_file_without_comma(inventory_module, monkeypatch):
    host_list = "host1"
    monkeypatch.setattr(os.path, "exists", lambda x: False)
    assert inventory_module.verify_file(host_list) == False

def test_parse_valid_host_list(inventory_module, monkeypatch):
    inventory = MockInventory()
    loader = MockLoader()
    host_list = "host1,host2"
    
    monkeypatch.setattr(inventory_module, "_expand_hostpattern", lambda x: ([x], None))
    inventory_module.parse(inventory, loader, host_list)
    
    assert "host1" in inventory.hosts
    assert "host2" in inventory.hosts

def test_parse_invalid_host_list(inventory_module, monkeypatch):
    inventory = MockInventory()
    loader = MockLoader()
    host_list = "invalid_host"
    
    def mock_expand_hostpattern(x):
        raise AnsibleError("Mock error")
    
    monkeypatch.setattr(inventory_module, "_expand_hostpattern", mock_expand_hostpattern)
    monkeypatch.setattr(inventory_module, "display", type('obj', (object,), {'vvv': lambda x: None}))
    
    inventory_module.parse(inventory, loader, host_list)
    
    assert "invalid_host" in inventory.hosts

def test_parse_raises_ansible_parser_error(inventory_module, monkeypatch):
    inventory = MockInventory()
    loader = MockLoader()
    host_list = "host1,host2"
    
    def mock_expand_hostpattern(x):
        raise Exception("Mock exception")
    
    monkeypatch.setattr(inventory_module, "_expand_hostpattern", mock_expand_hostpattern)
    
    with pytest.raises(AnsibleParserError, match="Invalid data from string, could not parse: Mock exception"):
        inventory_module.parse(inventory, loader, host_list)
