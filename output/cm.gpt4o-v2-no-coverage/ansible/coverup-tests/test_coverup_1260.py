# file: lib/ansible/plugins/inventory/generator.py:121-135
# asked: {"lines": [124, 126, 128, 129, 130, 131, 132, 133, 134, 135], "branches": [[129, 0], [129, 130], [131, 132], [131, 133]]}
# gained: {"lines": [124, 126, 128, 129, 130, 131, 132, 133, 134, 135], "branches": [[129, 0], [129, 130], [131, 132], [131, 133]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.inventory.generator import InventoryModule
from ansible.errors import AnsibleParserError

@pytest.fixture
def inventory():
    return MagicMock()

@pytest.fixture
def loader():
    return MagicMock()

@pytest.fixture
def path():
    return 'dummy_path'

@pytest.fixture
def config_data():
    return {
        'plugin': 'generator',
        'layers': {
            'layer1': ['a', 'b'],
            'layer2': ['1', '2']
        },
        'hosts': {
            'name': 'host_{{ layer1 }}_{{ layer2 }}',
            'parents': [{'name': 'parent_{{ layer1 }}', 'vars': {'var1': 'value1'}}]
        }
    }

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse(inventory_module, inventory, loader, path, config_data):
    with patch.object(inventory_module, '_read_config_data', return_value=config_data):
        with patch.object(inventory_module, 'template', side_effect=lambda x, y: x.replace('{{ layer1 }}', y['layer1']).replace('{{ layer2 }}', y['layer2'])):
            with patch.object(inventory_module, 'add_parents') as mock_add_parents:
                inventory_module.parse(inventory, loader, path)
                
                # Check if hosts are added correctly
                inventory.add_host.assert_any_call('host_a_1')
                inventory.add_host.assert_any_call('host_a_2')
                inventory.add_host.assert_any_call('host_b_1')
                inventory.add_host.assert_any_call('host_b_2')
                
                # Check if add_parents is called correctly
                assert mock_add_parents.call_count == 4
                mock_add_parents.assert_any_call(inventory, 'host_a_1', config_data['hosts']['parents'], {'layer1': 'a', 'layer2': '1'})
                mock_add_parents.assert_any_call(inventory, 'host_a_2', config_data['hosts']['parents'], {'layer1': 'a', 'layer2': '2'})
                mock_add_parents.assert_any_call(inventory, 'host_b_1', config_data['hosts']['parents'], {'layer1': 'b', 'layer2': '1'})
                mock_add_parents.assert_any_call(inventory, 'host_b_2', config_data['hosts']['parents'], {'layer1': 'b', 'layer2': '2'})

def test_add_parents(inventory_module, inventory):
    child = 'host_a_1'
    parents = [{'name': 'parent_{{ layer1 }}', 'vars': {'var1': 'value1'}}]
    template_vars = {'layer1': 'a', 'layer2': '1'}
    
    with patch.object(inventory_module, 'template', side_effect=lambda x, y: x.replace('{{ layer1 }}', y['layer1'])):
        inventory_module.add_parents(inventory, child, parents, template_vars)
        
        # Check if groups are added correctly
        inventory.add_group.assert_called_once_with('parent_a')
        
        # Check if variables are set correctly
        group = inventory.groups['parent_a']
        group.set_variable.assert_called_once_with('var1', 'value1')
        
        # Check if child is added to group
        inventory.add_child.assert_called_once_with('parent_a', child)
