# file lib/ansible/inventory/data.py:191-234
# lines [191, 194, 195, 196, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 211, 213, 214, 215, 218, 219, 220, 221, 223, 225, 227, 228, 229, 230, 232, 234]
# branches ['194->195', '194->232', '195->196', '195->199', '200->201', '200->206', '201->202', '201->204', '206->207', '206->225', '209->210', '209->213', '218->219', '218->227', '219->220', '219->223', '227->228', '227->234']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.utils.display import Display

# Mock the display object to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mock_display = mocker.patch('ansible.inventory.data.display', new_callable=Display)
    mock_display.debug = mocker.MagicMock()
    mock_display.vvvv = mocker.MagicMock()
    mock_display.warning = mocker.MagicMock()
    return mock_display

# Mock the C.LOCALHOST constant
@pytest.fixture
def mock_C_LOCALHOST(mocker):
    mocker.patch('ansible.inventory.data.C.LOCALHOST', ['localhost'])

# Test function to improve coverage
def test_add_host_to_inventory(mock_display, mock_C_LOCALHOST):
    inventory_data = InventoryData()

    # Add a group to inventory
    group_name = 'test_group'
    inventory_data.groups[group_name] = Group(group_name)

    # Add a host to inventory without a group
    host_name = 'test_host'
    inventory_data.add_host(host_name)
    assert host_name in inventory_data.hosts
    assert inventory_data.hosts[host_name].name == host_name

    # Add a host to inventory with a group
    inventory_data.add_host(host_name, group=group_name)
    assert group_name in inventory_data.groups
    assert inventory_data.hosts[host_name] in inventory_data.groups[group_name].get_hosts()

    # Add a localhost to inventory
    localhost_name = 'localhost'
    inventory_data.add_host(localhost_name)
    assert inventory_data.localhost.name == localhost_name

    # Add a duplicate localhost to inventory
    duplicate_localhost_name = 'localhost'
    inventory_data.add_host(duplicate_localhost_name)
    assert inventory_data.localhost.name == localhost_name

    # Attempt to add a host with an invalid name (non-string)
    with pytest.raises(AnsibleError):
        inventory_data.add_host(123)

    # Attempt to add a host with an empty name
    with pytest.raises(AnsibleError):
        inventory_data.add_host('')

    # Attempt to add a host to a non-existent group
    with pytest.raises(AnsibleError):
        inventory_data.add_host(host_name, group='non_existent_group')
