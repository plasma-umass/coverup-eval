# file: lib/ansible/plugins/inventory/advanced_host_list.py:31-63
# asked: {"lines": [], "branches": [[51, 49], [60, 59]]}
# gained: {"lines": [], "branches": [[51, 49]]}

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.inventory.advanced_host_list import InventoryModule
from unittest.mock import MagicMock, patch

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_verify_file_with_comma(inventory_module):
    assert inventory_module.verify_file("host1,host2") == True

def test_verify_file_without_comma(inventory_module):
    assert inventory_module.verify_file("host1") == False

def test_parse_with_valid_hosts(inventory_module, monkeypatch):
    inventory = MagicMock()
    loader = MagicMock()
    host_list = "host1,host2"
    
    monkeypatch.setattr(inventory_module, '_expand_hostpattern', lambda x: ([x], None))
    monkeypatch.setattr(inventory_module, 'inventory', inventory)
    
    inventory_module.parse(inventory, loader, host_list)
    
    inventory.add_host.assert_any_call("host1", group='ungrouped', port=None)
    inventory.add_host.assert_any_call("host2", group='ungrouped', port=None)

def test_parse_with_empty_host(inventory_module, monkeypatch):
    inventory = MagicMock()
    loader = MagicMock()
    host_list = "host1,,host2"
    
    monkeypatch.setattr(inventory_module, '_expand_hostpattern', lambda x: ([x], None))
    monkeypatch.setattr(inventory_module, 'inventory', inventory)
    
    inventory_module.parse(inventory, loader, host_list)
    
    inventory.add_host.assert_any_call("host1", group='ungrouped', port=None)
    inventory.add_host.assert_any_call("host2", group='ungrouped', port=None)
    assert inventory.add_host.call_count == 2

def test_parse_with_invalid_host(inventory_module, monkeypatch):
    inventory = MagicMock()
    loader = MagicMock()
    host_list = "host1,invalid_host"
    
    def mock_expand_hostpattern(host):
        if host == "invalid_host":
            raise AnsibleError("Invalid host")
        return ([host], None)
    
    monkeypatch.setattr(inventory_module, '_expand_hostpattern', mock_expand_hostpattern)
    monkeypatch.setattr(inventory_module, 'inventory', inventory)
    monkeypatch.setattr(inventory_module.display, 'vvv', MagicMock())
    
    inventory_module.parse(inventory, loader, host_list)
    
    inventory.add_host.assert_any_call("host1", group='ungrouped', port=None)
    inventory.add_host.assert_any_call("invalid_host", group='ungrouped', port=None)
    inventory_module.display.vvv.assert_called_with("Unable to parse address from hostname, leaving unchanged: Invalid host")

def test_parse_with_exception(inventory_module, monkeypatch):
    inventory = MagicMock()
    loader = MagicMock()
    host_list = "host1,host2"
    
    def mock_expand_hostpattern(host):
        raise Exception("Unexpected error")
    
    monkeypatch.setattr(inventory_module, '_expand_hostpattern', mock_expand_hostpattern)
    monkeypatch.setattr(inventory_module, 'inventory', inventory)
    
    with pytest.raises(AnsibleParserError, match="Invalid data from string, could not parse: Unexpected error"):
        inventory_module.parse(inventory, loader, host_list)
