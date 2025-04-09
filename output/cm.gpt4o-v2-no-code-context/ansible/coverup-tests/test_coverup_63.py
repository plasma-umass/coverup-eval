# file: lib/ansible/plugins/inventory/constructed.py:137-177
# asked: {"lines": [137, 140, 142, 144, 145, 146, 147, 148, 149, 151, 152, 153, 155, 158, 159, 160, 163, 166, 167, 168, 171, 174, 176, 177], "branches": [[148, 149], [148, 151], [155, 0], [155, 158], [159, 160], [159, 163], [167, 168], [167, 171]]}
# gained: {"lines": [137, 140, 142, 144, 145, 146, 147, 148, 149, 151, 152, 153, 155, 158, 159, 163, 166, 167, 171, 174, 176, 177], "branches": [[148, 149], [155, 0], [155, 158], [159, 163], [167, 171]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.errors import AnsibleOptionsError, AnsibleParserError
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.hostvars import HostVars
from ansible.utils.vars import combine_vars

@pytest.fixture
def inventory():
    inventory = MagicMock(spec=InventoryManager)
    inventory.hosts = {
        'host1': MagicMock(),
        'host2': MagicMock()
    }
    inventory.processed_sources = ['source1']
    return inventory

@pytest.fixture
def loader():
    return MagicMock(spec=DataLoader)

@pytest.fixture
def path():
    return 'dummy_path'

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_with_processed_sources(inventory_module, inventory, loader, path, monkeypatch):
    monkeypatch.setattr(inventory_module, '_read_config_data', MagicMock())
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: True if x == 'strict' else False)
    monkeypatch.setattr(inventory_module, '_set_composite_vars', MagicMock())
    monkeypatch.setattr(inventory_module, '_add_host_to_composed_groups', MagicMock())
    monkeypatch.setattr(inventory_module, '_add_host_to_keyed_groups', MagicMock())
    monkeypatch.setattr(inventory_module, 'get_all_host_vars', lambda *args: {})
    monkeypatch.setattr(inventory_module, '_cache', {})

    inventory_module.parse(inventory, loader, path)

    inventory_module._read_config_data.assert_called_once_with(path)
    assert inventory_module._set_composite_vars.call_count == 2
    assert inventory_module._add_host_to_composed_groups.call_count == 2
    assert inventory_module._add_host_to_keyed_groups.call_count == 2

def test_parse_without_processed_sources(inventory_module, inventory, loader, path, monkeypatch):
    del inventory.processed_sources
    monkeypatch.setattr(inventory_module, '_read_config_data', MagicMock())
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: True if x == 'use_vars_plugins' else False)

    with pytest.raises(AnsibleOptionsError, match="The option use_vars_plugins requires ansible >= 2.11."):
        inventory_module.parse(inventory, loader, path)

def test_parse_with_exception(inventory_module, inventory, loader, path, monkeypatch):
    monkeypatch.setattr(inventory_module, '_read_config_data', MagicMock())
    monkeypatch.setattr(inventory_module, 'get_option', lambda x: True if x == 'strict' else False)
    monkeypatch.setattr(inventory_module, '_set_composite_vars', MagicMock(side_effect=Exception('test exception')))
    monkeypatch.setattr(inventory_module, 'get_all_host_vars', lambda *args: {})

    with pytest.raises(AnsibleParserError, match="failed to parse dummy_path: test exception"):
        inventory_module.parse(inventory, loader, path)
