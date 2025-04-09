# file: lib/ansible/plugins/inventory/toml.py:155-197
# asked: {"lines": [155, 156, 157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 171, 172, 174, 175, 176, 177, 178, 180, 181, 182, 184, 185, 186, 187, 188, 190, 191, 192, 194, 195, 196], "branches": [[156, 157], [156, 160], [161, 162], [161, 164], [164, 0], [164, 165], [165, 166], [165, 174], [166, 167], [166, 171], [171, 164], [171, 172], [174, 175], [174, 184], [175, 176], [175, 180], [180, 164], [180, 181], [184, 185], [184, 194], [185, 186], [185, 190], [190, 164], [190, 191]]}
# gained: {"lines": [155, 156, 157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 171, 172, 174, 175, 176, 177, 178, 180, 181, 182, 184, 185, 186, 187, 188, 190, 191, 192, 194, 195, 196], "branches": [[156, 157], [156, 160], [161, 162], [161, 164], [164, 0], [164, 165], [165, 166], [165, 174], [166, 167], [166, 171], [171, 164], [171, 172], [174, 175], [174, 184], [175, 176], [175, 180], [180, 164], [180, 181], [184, 185], [184, 194], [185, 186], [185, 190], [190, 164], [190, 191]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.inventory.toml import InventoryModule
from ansible.errors import AnsibleParserError
from collections.abc import MutableMapping, MutableSequence

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.display = MagicMock()
    module.inventory = MagicMock()
    return module

def test_parse_group_invalid_group_data(inventory_module):
    inventory_module._parse_group('invalid_group', 'not_a_dict')
    inventory_module.display.warning.assert_called_once_with("Skipping 'invalid_group' as this is not a valid group definition")

def test_parse_group_none_group_data(inventory_module):
    inventory_module._parse_group('none_group', None)
    inventory_module.inventory.add_group.assert_called_once_with('none_group')

def test_parse_group_vars_invalid_type(inventory_module):
    with pytest.raises(AnsibleParserError, match=r'Invalid "vars" entry for "<MagicMock.*>" group, requires a dict, found "<class \'str\'>" instead.'):
        inventory_module._parse_group('vars_group', {'vars': 'not_a_dict'})

def test_parse_group_vars_valid(inventory_module):
    group_mock = MagicMock()
    inventory_module.inventory.add_group.return_value = 'vars_group'
    inventory_module._parse_group('vars_group', {'vars': {'var1': 'value1'}})
    inventory_module.inventory.set_variable.assert_called_once_with('vars_group', 'var1', 'value1')

def test_parse_group_children_invalid_type(inventory_module):
    with pytest.raises(AnsibleParserError, match=r'Invalid "children" entry for "<MagicMock.*>" group, requires a list, found "<class \'str\'>" instead.'):
        inventory_module._parse_group('children_group', {'children': 'not_a_list'})

def test_parse_group_children_valid(inventory_module):
    group_mock = MagicMock()
    inventory_module.inventory.add_group.return_value = 'children_group'
    inventory_module._parse_group('children_group', {'children': ['subgroup1']})
    inventory_module.inventory.add_child.assert_called_once_with('children_group', 'subgroup1')

def test_parse_group_hosts_invalid_type(inventory_module):
    with pytest.raises(AnsibleParserError, match=r'Invalid "hosts" entry for "<MagicMock.*>" group, requires a dict, found "<class \'str\'>" instead.'):
        inventory_module._parse_group('hosts_group', {'hosts': 'not_a_dict'})

def test_parse_group_hosts_valid(inventory_module):
    group_mock = MagicMock()
    inventory_module.inventory.add_group.return_value = 'hosts_group'
    with patch.object(inventory_module, '_expand_hostpattern', return_value=(['host1'], None)), \
         patch.object(inventory_module, '_populate_host_vars') as mock_populate_host_vars:
        inventory_module._parse_group('hosts_group', {'hosts': {'host1': 'value1'}})
        mock_populate_host_vars.assert_called_once_with(['host1'], 'value1', 'hosts_group', None)

def test_parse_group_unexpected_key(inventory_module):
    group_mock = MagicMock()
    inventory_module.inventory.add_group.return_value = 'unexpected_key_group'
    inventory_module._parse_group('unexpected_key_group', {'unexpected': 'value'})
    inventory_module.display.warning.assert_called_once_with('Skipping unexpected key "unexpected" in group "unexpected_key_group", only "vars", "children" and "hosts" are valid')
