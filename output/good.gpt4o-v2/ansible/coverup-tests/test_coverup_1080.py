# file: lib/ansible/plugins/inventory/toml.py:155-197
# asked: {"lines": [156, 157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 171, 172, 174, 175, 176, 177, 178, 180, 181, 182, 184, 185, 186, 187, 188, 190, 191, 192, 194, 195, 196], "branches": [[156, 157], [156, 160], [161, 162], [161, 164], [164, 0], [164, 165], [165, 166], [165, 174], [166, 167], [166, 171], [171, 164], [171, 172], [174, 175], [174, 184], [175, 176], [175, 180], [180, 164], [180, 181], [184, 185], [184, 194], [185, 186], [185, 190], [190, 164], [190, 191]]}
# gained: {"lines": [156, 157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 171, 172, 174, 175, 176, 177, 178, 180, 181, 182, 184, 185, 186, 187, 188, 190, 191, 192, 194, 195, 196], "branches": [[156, 157], [156, 160], [161, 162], [161, 164], [164, 0], [164, 165], [165, 166], [165, 174], [166, 167], [166, 171], [171, 164], [171, 172], [174, 175], [174, 184], [175, 176], [175, 180], [180, 164], [180, 181], [184, 185], [184, 194], [185, 186], [185, 190], [190, 164], [190, 191]]}

import pytest
from unittest.mock import MagicMock
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.toml import InventoryModule
from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.display = MagicMock()
    module.inventory = MagicMock()
    return module

def test_parse_group_invalid_group_data(inventory_module):
    inventory_module._parse_group('test_group', 'invalid_data')
    inventory_module.display.warning.assert_called_once_with("Skipping 'test_group' as this is not a valid group definition")

def test_parse_group_none_group_data(inventory_module):
    inventory_module.inventory.add_group.return_value = 'test_group'
    inventory_module._parse_group('test_group', None)
    inventory_module.inventory.add_group.assert_called_once_with('test_group')

def test_parse_group_invalid_vars_entry(inventory_module):
    inventory_module.inventory.add_group.return_value = 'test_group'
    with pytest.raises(AnsibleParserError, match='Invalid "vars" entry for "test_group" group, requires a dict, found "<class \'str\'>" instead.'):
        inventory_module._parse_group('test_group', {'vars': 'invalid_data'})

def test_parse_group_valid_vars_entry(inventory_module):
    inventory_module.inventory.add_group.return_value = 'test_group'
    inventory_module._parse_group('test_group', {'vars': {'var1': 'value1'}})
    inventory_module.inventory.set_variable.assert_called_once_with('test_group', 'var1', 'value1')

def test_parse_group_invalid_children_entry(inventory_module):
    inventory_module.inventory.add_group.return_value = 'test_group'
    with pytest.raises(AnsibleParserError, match='Invalid "children" entry for "test_group" group, requires a list, found "<class \'str\'>" instead.'):
        inventory_module._parse_group('test_group', {'children': 'invalid_data'})

def test_parse_group_valid_children_entry(inventory_module):
    inventory_module.inventory.add_group.return_value = 'test_group'
    inventory_module._parse_group('test_group', {'children': ['child_group']})
    inventory_module.inventory.add_child.assert_called_once_with('test_group', 'child_group')

def test_parse_group_invalid_hosts_entry(inventory_module):
    inventory_module.inventory.add_group.return_value = 'test_group'
    with pytest.raises(AnsibleParserError, match='Invalid "hosts" entry for "test_group" group, requires a dict, found "<class \'str\'>" instead.'):
        inventory_module._parse_group('test_group', {'hosts': 'invalid_data'})

def test_parse_group_valid_hosts_entry(inventory_module, monkeypatch):
    inventory_module.inventory.add_group.return_value = 'test_group'
    mock_expand_hostpattern = MagicMock(return_value=(['host1'], None))
    mock_populate_host_vars = MagicMock()
    monkeypatch.setattr(inventory_module, '_expand_hostpattern', mock_expand_hostpattern)
    monkeypatch.setattr(inventory_module, '_populate_host_vars', mock_populate_host_vars)
    inventory_module._parse_group('test_group', {'hosts': {'host_pattern': 'value'}})
    mock_expand_hostpattern.assert_called_once_with('host_pattern')
    mock_populate_host_vars.assert_called_once_with(['host1'], 'value', 'test_group', None)

def test_parse_group_unexpected_key(inventory_module):
    inventory_module.inventory.add_group.return_value = 'test_group'
    inventory_module._parse_group('test_group', {'unexpected_key': 'value'})
    inventory_module.display.warning.assert_called_once_with('Skipping unexpected key "unexpected_key" in group "test_group", only "vars", "children" and "hosts" are valid')
