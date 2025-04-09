# file: lib/ansible/plugins/inventory/toml.py:155-197
# asked: {"lines": [155, 156, 157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 171, 172, 174, 175, 176, 177, 178, 180, 181, 182, 184, 185, 186, 187, 188, 190, 191, 192, 194, 195, 196], "branches": [[156, 157], [156, 160], [161, 162], [161, 164], [164, 0], [164, 165], [165, 166], [165, 174], [166, 167], [166, 171], [171, 164], [171, 172], [174, 175], [174, 184], [175, 176], [175, 180], [180, 164], [180, 181], [184, 185], [184, 194], [185, 186], [185, 190], [190, 164], [190, 191]]}
# gained: {"lines": [155, 156, 157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 171, 172, 174, 175, 176, 177, 178, 180, 181, 182, 184, 185, 186, 187, 188, 190, 191, 192, 194, 195, 196], "branches": [[156, 157], [156, 160], [161, 162], [161, 164], [164, 0], [164, 165], [165, 166], [165, 174], [166, 167], [166, 171], [171, 164], [171, 172], [174, 175], [174, 184], [175, 176], [175, 180], [180, 164], [180, 181], [184, 185], [184, 194], [185, 186], [185, 190], [190, 164], [190, 191]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.toml import InventoryModule
from collections.abc import MutableMapping, MutableSequence

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.inventory = MagicMock()
    module.display = MagicMock()
    return module

def test_parse_group_with_invalid_group_data(inventory_module):
    inventory_module._parse_group('group1', 'invalid_data')
    inventory_module.display.warning.assert_called_once_with("Skipping 'group1' as this is not a valid group definition")

def test_parse_group_with_none_group_data(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    inventory_module._parse_group('group1', None)
    inventory_module.inventory.add_group.assert_called_once_with('group1')

def test_parse_group_with_valid_vars(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    group_data = {'vars': {'var1': 'value1'}}
    inventory_module._parse_group('group1', group_data)
    inventory_module.inventory.set_variable.assert_called_once_with('group1', 'var1', 'value1')

def test_parse_group_with_invalid_vars(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    group_data = {'vars': 'invalid_data'}
    with pytest.raises(AnsibleParserError, match='Invalid "vars" entry for "group1" group, requires a dict, found ".*" instead.'):
        inventory_module._parse_group('group1', group_data)

def test_parse_group_with_valid_children(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    group_data = {'children': ['child1']}
    inventory_module._parse_group('group1', group_data)
    inventory_module.inventory.add_child.assert_called_once_with('group1', 'child1')

def test_parse_group_with_invalid_children(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    group_data = {'children': 'invalid_data'}
    with pytest.raises(AnsibleParserError, match='Invalid "children" entry for "group1" group, requires a list, found ".*" instead.'):
        inventory_module._parse_group('group1', group_data)

def test_parse_group_with_valid_hosts(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    group_data = {'hosts': {'host1': 'value1'}}
    with patch.object(inventory_module, '_expand_hostpattern', return_value=(['host1'], None)), \
         patch.object(inventory_module, '_populate_host_vars') as mock_populate_host_vars:
        inventory_module._parse_group('group1', group_data)
        mock_populate_host_vars.assert_called_once_with(['host1'], 'value1', 'group1', None)

def test_parse_group_with_invalid_hosts(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    group_data = {'hosts': 'invalid_data'}
    with pytest.raises(AnsibleParserError, match='Invalid "hosts" entry for "group1" group, requires a dict, found ".*" instead.'):
        inventory_module._parse_group('group1', group_data)

def test_parse_group_with_unexpected_key(inventory_module):
    inventory_module.inventory.add_group.return_value = 'group1'
    group_data = {'unexpected_key': 'value1'}
    inventory_module._parse_group('group1', group_data)
    inventory_module.display.warning.assert_called_once_with('Skipping unexpected key "unexpected_key" in group "group1", only "vars", "children" and "hosts" are valid')
