# file: lib/ansible/plugins/inventory/constructed.py:137-177
# asked: {"lines": [140, 142, 144, 145, 146, 147, 148, 149, 151, 152, 153, 155, 158, 159, 160, 163, 166, 167, 168, 171, 174, 176, 177], "branches": [[148, 149], [148, 151], [155, 0], [155, 158], [159, 160], [159, 163], [167, 168], [167, 171]]}
# gained: {"lines": [140, 142, 144, 145, 146, 147, 148, 149, 151, 152, 153, 155, 158, 159, 163, 166, 167, 171, 174, 176, 177], "branches": [[148, 149], [155, 0], [155, 158], [159, 163], [167, 171]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError, AnsibleOptionsError
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def inventory():
    class Inventory:
        def __init__(self):
            self.hosts = {
                'host1': {},
                'host2': {}
            }
            self.processed_sources = ['source1', 'source2']
    return Inventory()

@pytest.fixture
def loader():
    return MagicMock()

@pytest.fixture
def path():
    return 'dummy_path'

@pytest.fixture
def fact_cache():
    return FactCache()

def test_parse_with_processed_sources(inventory, loader, path, fact_cache, monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, 'get_option', lambda x: True if x in ['strict', 'compose', 'groups', 'keyed_groups'] else False)
    monkeypatch.setattr(module, '_read_config_data', lambda x: None)
    monkeypatch.setattr(module, 'get_all_host_vars', lambda *args: {})
    monkeypatch.setattr(module, '_set_composite_vars', lambda compose, variables, host, strict: None)
    monkeypatch.setattr(module, '_add_host_to_composed_groups', lambda groups, variables, host, strict, fetch_hostvars: None)
    monkeypatch.setattr(module, '_add_host_to_keyed_groups', lambda keys, variables, host, strict, fetch_hostvars: None)
    monkeypatch.setattr(module, '_cache', {})

    module.parse(inventory, loader, path)

    assert True  # If no exception is raised, the test passes

def test_parse_without_processed_sources(inventory, loader, path, fact_cache, monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, 'get_option', lambda x: True if x == 'use_vars_plugins' else False)
    monkeypatch.setattr(module, '_read_config_data', lambda x: None)
    monkeypatch.setattr(module, 'get_all_host_vars', lambda *args: {})
    monkeypatch.setattr(module, '_set_composite_vars', lambda compose, variables, host, strict: None)
    monkeypatch.setattr(module, '_add_host_to_composed_groups', lambda groups, variables, host, strict, fetch_hostvars: None)
    monkeypatch.setattr(module, '_add_host_to_keyed_groups', lambda keys, variables, host, strict, fetch_hostvars: None)
    monkeypatch.setattr(module, '_cache', {})

    del inventory.processed_sources

    with pytest.raises(AnsibleOptionsError, match="The option use_vars_plugins requires ansible >= 2.11."):
        module.parse(inventory, loader, path)

def test_parse_with_exception(inventory, loader, path, fact_cache, monkeypatch):
    module = InventoryModule()
    monkeypatch.setattr(module, 'get_option', lambda x: True if x in ['strict', 'compose', 'groups', 'keyed_groups'] else False)
    monkeypatch.setattr(module, '_read_config_data', lambda x: None)
    monkeypatch.setattr(module, 'get_all_host_vars', lambda *args: {})
    monkeypatch.setattr(module, '_set_composite_vars', lambda compose, variables, host, strict: None)
    monkeypatch.setattr(module, '_add_host_to_composed_groups', lambda groups, variables, host, strict, fetch_hostvars: None)
    monkeypatch.setattr(module, '_add_host_to_keyed_groups', lambda keys, variables, host, strict, fetch_hostvars: None)
    monkeypatch.setattr(module, '_cache', {})
    monkeypatch.setattr(module, 'get_all_host_vars', lambda *args: (_ for _ in ()).throw(Exception('Test Exception')))

    with pytest.raises(AnsibleParserError, match="failed to parse dummy_path: Test Exception"):
        module.parse(inventory, loader, path)
