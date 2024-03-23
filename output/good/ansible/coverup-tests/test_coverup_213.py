# file lib/ansible/inventory/data.py:258-273
# lines [258, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 272, 273]
# branches ['261->262', '261->272', '263->264', '263->265', '265->266', '265->268']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from ansible.utils.display import Display

# Mock the display object to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    mock = mocker.patch('ansible.inventory.data.display', new_callable=Display)
    mock.debug = mocker.MagicMock()
    return mock

# Test function to cover add_child method
def test_add_child(mock_display):
    inventory_data = InventoryData()

    # Setup groups and hosts
    parent_group = Group('parent')
    child_group = Group('child_group')
    child_host = Host('child_host')

    # Add groups and hosts to inventory
    inventory_data.groups[parent_group.name] = parent_group
    inventory_data.groups[child_group.name] = child_group
    inventory_data.hosts[child_host.name] = child_host

    # Test adding a child group
    added_group = inventory_data.add_child('parent', 'child_group')
    assert added_group is True
    assert child_group in parent_group.child_groups
    mock_display.debug.assert_called_with('Group parent now contains child_group')

    # Test adding a child host
    added_host = inventory_data.add_child('parent', 'child_host')
    assert added_host is True
    assert child_host in parent_group.hosts
    mock_display.debug.assert_called_with('Group parent now contains child_host')

    # Test adding a non-existent child
    with pytest.raises(AnsibleError) as excinfo:
        inventory_data.add_child('parent', 'non_existent')
    assert "non_existent is not a known host nor group" in str(excinfo.value)

    # Test adding a child to a non-existent group
    with pytest.raises(AnsibleError) as excinfo:
        inventory_data.add_child('non_existent', 'child_group')
    assert "non_existent is not a known group" in str(excinfo.value)

    # Cleanup
    del inventory_data.groups[parent_group.name]
    del inventory_data.groups[child_group.name]
    del inventory_data.hosts[child_host.name]
