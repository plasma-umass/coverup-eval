# file lib/ansible/plugins/inventory/generator.py:107-119
# lines [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
# branches ['108->exit', '108->109', '113->114', '113->115', '116->117', '116->118']

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.errors import AnsibleParserError
from unittest.mock import MagicMock

@pytest.fixture
def inventory():
    inventory = MagicMock()
    inventory.groups = {}
    inventory.add_group = MagicMock(side_effect=lambda groupname: inventory.groups.setdefault(groupname, MagicMock()))
    inventory.add_child = MagicMock()
    return inventory

@pytest.fixture
def template_vars():
    return {'var1': 'value1'}

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_add_parents_with_invalid_parent_name(inventory_module, inventory, template_vars):
    child = {'name': 'child1'}
    parents = [{'name': None}]
    
    with pytest.raises(AnsibleParserError, match="Element child1 has a parent with no name element"):
        inventory_module.add_parents(inventory, child, parents, template_vars)

def test_add_parents_with_valid_parent(inventory_module, inventory, template_vars):
    child = {'name': 'child1'}
    parents = [{'name': 'parent1', 'vars': {'key1': 'value1'}, 'parents': []}]
    
    inventory_module.template = MagicMock(side_effect=lambda x, y: x)
    
    inventory_module.add_parents(inventory, child, parents, template_vars)
    
    inventory.add_group.assert_called_once_with('parent1')
    inventory.add_child.assert_called_once_with('parent1', child)
    assert 'parent1' in inventory.groups
    inventory.groups['parent1'].set_variable.assert_called_once_with('key1', 'value1')

def test_add_parents_with_nested_parents(inventory_module, inventory, template_vars):
    child = {'name': 'child1'}
    parents = [{'name': 'parent1', 'vars': {'key1': 'value1'}, 'parents': [{'name': 'grandparent1'}]}]
    
    inventory_module.template = MagicMock(side_effect=lambda x, y: x)
    
    inventory_module.add_parents(inventory, child, parents, template_vars)
    
    inventory.add_group.assert_any_call('parent1')
    inventory.add_group.assert_any_call('grandparent1')
    inventory.add_child.assert_any_call('parent1', child)
    inventory.add_child.assert_any_call('grandparent1', 'parent1')
    assert 'parent1' in inventory.groups
    assert 'grandparent1' in inventory.groups
    inventory.groups['parent1'].set_variable.assert_called_once_with('key1', 'value1')
