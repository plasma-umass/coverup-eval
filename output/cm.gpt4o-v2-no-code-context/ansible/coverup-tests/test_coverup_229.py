# file: lib/ansible/plugins/inventory/generator.py:121-135
# asked: {"lines": [121, 124, 126, 128, 129, 130, 131, 132, 133, 134, 135], "branches": [[129, 0], [129, 130], [131, 132], [131, 133]]}
# gained: {"lines": [121, 124, 126, 128, 129, 130, 131, 132, 133, 134, 135], "branches": [[129, 0], [129, 130], [131, 132], [131, 133]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.inventory.generator import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_path():
    return 'dummy_path'

@pytest.fixture
def mock_config_data():
    return {
        'layers': {
            'layer1': ['value1', 'value2'],
            'layer2': ['value3', 'value4']
        },
        'hosts': {
            'name': 'host_{{ layer1 }}_{{ layer2 }}',
            'parents': ['parent1', 'parent2']
        }
    }

@patch('ansible.plugins.inventory.generator.InventoryModule._read_config_data')
@patch('ansible.plugins.inventory.generator.InventoryModule.template')
@patch('ansible.plugins.inventory.generator.InventoryModule.add_parents')
def test_parse(mock_add_parents, mock_template, mock_read_config_data, inventory_module, mock_inventory, mock_loader, mock_path, mock_config_data):
    mock_read_config_data.return_value = mock_config_data
    mock_template.side_effect = lambda name, vars: name.replace('{{ layer1 }}', vars['layer1']).replace('{{ layer2 }}', vars['layer2'])

    inventory_module.parse(mock_inventory, mock_loader, mock_path)

    mock_read_config_data.assert_called_once_with(mock_path)
    assert mock_template.call_count == 4
    assert mock_inventory.add_host.call_count == 4
    assert mock_add_parents.call_count == 4

    expected_hosts = [
        'host_value1_value3',
        'host_value1_value4',
        'host_value2_value3',
        'host_value2_value4'
    ]

    for host in expected_hosts:
        mock_inventory.add_host.assert_any_call(host)
        mock_add_parents.assert_any_call(mock_inventory, host, ['parent1', 'parent2'], {'layer1': host.split('_')[1], 'layer2': host.split('_')[2]})
