# file lib/ansible/inventory/data.py:104-146
# lines [104, 107, 108, 110, 112, 113, 114, 117, 118, 120, 122, 123, 125, 127, 129, 130, 132, 134, 135, 136, 139, 140, 143, 144, 146]
# branches ['112->113', '112->120', '117->112', '117->118', '122->123', '122->143', '127->129', '127->132', '129->130', '129->139', '132->134', '132->139', '135->136', '135->139', '139->122', '139->140', '143->144', '143->146']

import pytest
from ansible.inventory.data import InventoryData
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from ansible.utils.display import Display

# Mock the Display class to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')
    mocker.patch.object(Display, 'warning')

@pytest.fixture
def inventory_data():
    inventory_data = InventoryData()
    # Add 'all' and 'ungrouped' groups as they are expected to exist
    inventory_data.groups['all'] = Group('all')
    inventory_data.groups['ungrouped'] = Group('ungrouped')
    return inventory_data

def test_reconcile_inventory_with_conflict(mock_display, inventory_data):
    # Create a group and a host with the same name to test the conflict warning
    conflicting_name = "conflict"
    group = Group(conflicting_name)
    host = Host(conflicting_name)
    host.implicit = False  # Ensure the host is not implicit

    # Add the group and host to the inventory
    inventory_data.groups[group.name] = group
    inventory_data.hosts[host.name] = host

    # Run the reconcile_inventory method
    inventory_data.reconcile_inventory()

    # Check that the warning for the conflict was called
    Display.warning.assert_called_once_with("Found both group and host with same name: conflict")

    # Check that 'all' is an ancestor of the group
    assert inventory_data.groups['all'] in group.get_ancestors()

    # Check that the host is not in 'ungrouped' since it's not implicit
    assert host not in inventory_data.groups['ungrouped'].get_hosts()

    # Clean up the inventory data
    inventory_data.groups.clear()
    inventory_data.hosts.clear()
    inventory_data._groups_dict_cache.clear()
