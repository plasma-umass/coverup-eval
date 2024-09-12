# file: lib/ansible/inventory/data.py:160-178
# asked: {"lines": [160, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 176, 178], "branches": [[163, 164], [163, 176], [164, 165], [164, 166], [166, 167], [166, 174], [168, 169], [168, 172]]}
# gained: {"lines": [160, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 176, 178], "branches": [[163, 164], [163, 176], [164, 165], [164, 166], [166, 167], [166, 174], [168, 169]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.group import Group
from ansible.utils.display import Display

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_add_group_valid_new_group(monkeypatch, inventory_data):
    group_name = "new_group"
    inventory_data.groups = {}
    display = Display()

    def mock_debug(msg):
        assert msg == f"Added group {group_name} to inventory"

    monkeypatch.setattr(display, "debug", mock_debug)

    result = inventory_data.add_group(group_name)
    assert result == group_name
    assert group_name in inventory_data.groups
    assert isinstance(inventory_data.groups[group_name], Group)
    assert inventory_data._groups_dict_cache == {}

def test_add_group_existing_group(monkeypatch, inventory_data):
    group_name = "existing_group"
    inventory_data.groups = {group_name: Group(group_name)}
    display = Display()

    def mock_debug(msg):
        assert msg == f"group {group_name} already in inventory"

    monkeypatch.setattr(display, "debug", mock_debug)

    result = inventory_data.add_group(group_name)
    assert result == group_name
    assert group_name in inventory_data.groups

def test_add_group_invalid_group_type(inventory_data):
    with pytest.raises(AnsibleError) as excinfo:
        inventory_data.add_group(123)
    assert "Invalid group name supplied, expected a string but got" in str(excinfo.value)

def test_add_group_empty_group(inventory_data):
    with pytest.raises(AnsibleError) as excinfo:
        inventory_data.add_group("")
    assert "Invalid empty/false group name provided" in str(excinfo.value)
