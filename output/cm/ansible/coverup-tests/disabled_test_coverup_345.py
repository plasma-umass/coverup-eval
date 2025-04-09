# file lib/ansible/plugins/inventory/generator.py:121-135
# lines [121, 124, 126, 128, 129, 130, 131, 132, 133, 134, 135]
# branches ['129->exit', '129->130', '131->132', '131->133']

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from unittest.mock import MagicMock

@pytest.fixture
def inventory_module():
    inventory_manager = InventoryManager(loader=DataLoader())
    inventory_module = InventoryModule()
    inventory_module.inventory = inventory_manager
    inventory_module.loader = DataLoader()
    # Set the _redirected_names attribute to avoid AttributeError
    inventory_module._redirected_names = []
    return inventory_module

def test_inventory_module_parse(inventory_module, tmp_path, mocker):
    # Create a temporary inventory file with test data
    inventory_file = tmp_path / "test_inventory.yml"
    inventory_file.write_text("""
    layers:
      layer1: ['value1', 'value2']
      layer2: ['value3', 'value4']
    hosts:
      name: "{{ layer1 }}-{{ layer2 }}"
      parents: ['group1', 'group2']
    """)

    # Mock the template method to return the host name with templating
    mocker.patch.object(inventory_module, 'template', side_effect=lambda name, vars: name.replace("{{ layer1 }}", vars['layer1']).replace("{{ layer2 }}", vars['layer2']))
    # Mock the add_parents method to do nothing
    mocker.patch.object(inventory_module, 'add_parents')
    # Mock the _read_config_data method to return a dictionary
    mocker.patch.object(inventory_module, '_read_config_data', return_value={
        'layers': {
            'layer1': ['value1', 'value2'],
            'layer2': ['value3', 'value4']
        },
        'hosts': {
            'name': "{{ layer1 }}-{{ layer2 }}",
            'parents': ['group1', 'group2']
        }
    })

    # Call the parse method
    inventory_module.parse(
        inventory=inventory_module.inventory,
        loader=inventory_module.loader,
        path=str(inventory_file),
        cache=False
    )

    # Check if hosts are added correctly
    assert inventory_module.inventory.get_host('value1-value3') is not None
    assert inventory_module.inventory.get_host('value1-value4') is not None
    assert inventory_module.inventory.get_host('value2-value3') is not None
    assert inventory_module.inventory.get_host('value2-value4') is not None

    # Check if add_parents was called with correct parameters
    inventory_module.add_parents.assert_any_call(
        inventory_module.inventory,
        'value1-value3',
        ['group1', 'group2'],
        {'layer1': 'value1', 'layer2': 'value3'}
    )
    inventory_module.add_parents.assert_any_call(
        inventory_module.inventory,
        'value1-value4',
        ['group1', 'group2'],
        {'layer1': 'value1', 'layer2': 'value4'}
    )
    inventory_module.add_parents.assert_any_call(
        inventory_module.inventory,
        'value2-value3',
        ['group1', 'group2'],
        {'layer1': 'value2', 'layer2': 'value3'}
    )
    inventory_module.add_parents.assert_any_call(
        inventory_module.inventory,
        'value2-value4',
        ['group1', 'group2'],
        {'layer1': 'value2', 'layer2': 'value4'}
    )
