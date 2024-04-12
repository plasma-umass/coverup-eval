# file lib/ansible/inventory/data.py:160-178
# lines [160, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 176, 178]
# branches ['163->164', '163->176', '164->165', '164->166', '166->167', '166->174', '168->169', '168->172']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.group import Group
from ansible.utils.display import Display

# Mock the global display object to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mock = mocker.patch('ansible.inventory.data.display', new_callable=Display)
    mock.debug = mocker.MagicMock()
    return mock

def test_add_group_with_valid_name(mock_display):
    inventory_data = InventoryData()
    group_name = 'test_group'
    added_group_name = inventory_data.add_group(group_name)
    assert added_group_name == group_name
    assert group_name in inventory_data.groups
    mock_display.debug.assert_called_with("Added group %s to inventory" % group_name)

def test_add_group_with_existing_group(mock_display):
    inventory_data = InventoryData()
    group_name = 'test_group'
    inventory_data.add_group(group_name)  # Add the group first
    added_group_name = inventory_data.add_group(group_name)  # Try to add it again
    assert added_group_name == group_name
    mock_display.debug.assert_called_with("group %s already in inventory" % group_name)

def test_add_group_with_invalid_name_type(mock_display):
    inventory_data = InventoryData()
    group_name = 123  # Not a string
    with pytest.raises(AnsibleError) as excinfo:
        inventory_data.add_group(group_name)
    assert "Invalid group name supplied, expected a string but got" in str(excinfo.value)

def test_add_group_with_empty_name(mock_display):
    inventory_data = InventoryData()
    group_name = ''  # Empty string
    with pytest.raises(AnsibleError) as excinfo:
        inventory_data.add_group(group_name)
    assert "Invalid empty/false group name provided:" in str(excinfo.value)
