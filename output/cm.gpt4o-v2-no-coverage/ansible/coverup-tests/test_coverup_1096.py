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

class MockDisplay:
    def vvv(self, msg):
        pass

@pytest.fixture
def inventory_module(monkeypatch):
    module = InventoryModule()
    module.inventory = MockInventory()
    module.display = MockDisplay()
    return module

def test_verify_file_exists(monkeypatch, inventory_module):
    def mock_exists(path):
        return True

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert not inventory_module.verify_file('some_path')

def test_verify_file_not_exists_with_comma(monkeypatch, inventory_module):
    def mock_exists(path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert inventory_module.verify_file('host1,host2')

def test_verify_file_not_exists_without_comma(monkeypatch, inventory_module):
    def mock_exists(path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert not inventory_module.verify_file('some_path')

def test_parse_valid_host_list(monkeypatch, inventory_module):
    def mock_expand_hostpattern(pattern):
        return [pattern], None

    monkeypatch.setattr(inventory_module, '_expand_hostpattern', mock_expand_hostpattern)
    inventory_module.parse(inventory_module.inventory, None, 'host1,host2')
    assert 'host1' in inventory_module.inventory.hosts
    assert 'host2' in inventory_module.inventory.hosts

def test_parse_invalid_host_list(monkeypatch, inventory_module):
    def mock_expand_hostpattern(pattern):
        raise AnsibleError('error')

    monkeypatch.setattr(inventory_module, '_expand_hostpattern', mock_expand_hostpattern)
    inventory_module.parse(inventory_module.inventory, None, 'host1,host2')
    assert 'host1' in inventory_module.inventory.hosts
    assert 'host2' in inventory_module.inventory.hosts

def test_parse_raises_ansible_parser_error(monkeypatch, inventory_module):
    def mock_expand_hostpattern(pattern):
        raise Exception('error')

    monkeypatch.setattr(inventory_module, '_expand_hostpattern', mock_expand_hostpattern)
    with pytest.raises(AnsibleParserError, match='Invalid data from string, could not parse: error'):
        inventory_module.parse(inventory_module.inventory, None, 'host1,host2')
