# file lib/ansible/inventory/data.py:191-234
# lines [194, 195, 196, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 211, 213, 214, 215, 218, 219, 220, 221, 223, 225, 227, 228, 229, 230, 232, 234]
# branches ['194->195', '194->232', '195->196', '195->199', '200->201', '200->206', '201->202', '201->204', '206->207', '206->225', '209->210', '209->213', '218->219', '218->227', '219->220', '219->223', '227->228', '227->234']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.module_utils._text import to_text
from ansible.utils.display import Display

# Mock the display object to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mock_display = mocker.patch('ansible.inventory.data.display', new_callable=Display)
    mock_display.debug = mocker.MagicMock()
    mock_display.warning = mocker.MagicMock()
    mock_display.vvvv = mocker.MagicMock()
    return mock_display

# Test function to cover lines 194-234
def test_add_host_to_inventory_data(mock_display):
    inventory_data = InventoryData()

    # Test adding a valid host without a group
    host_name = 'test_host'
    inventory_data.add_host(host_name)
    assert host_name in inventory_data.hosts
    assert isinstance(inventory_data.hosts[host_name], Host)

    # Test adding a valid host with a group
    group_name = 'test_group'
    inventory_data.groups[group_name] = Group(group_name)
    inventory_data.add_host(host_name, group=group_name)
    assert host_name in [h.name for h in inventory_data.groups[group_name].get_hosts()]

    # Test adding a host with a non-existent group
    with pytest.raises(AnsibleError):
        inventory_data.add_host(host_name, group='non_existent_group')

    # Test adding a host with an invalid name (non-string)
    with pytest.raises(AnsibleError):
        inventory_data.add_host(123)

    # Test adding a host with an empty name
    with pytest.raises(AnsibleError):
        inventory_data.add_host('')

    # Test adding a localhost-like host
    localhost_name = 'localhost'
    inventory_data.add_host(localhost_name)
    assert inventory_data.localhost == inventory_data.hosts[localhost_name]

    # Test adding a duplicate localhost-like host
    duplicate_localhost_name = '127.0.0.1'
    inventory_data.add_host(duplicate_localhost_name)
    assert mock_display.warning.called

    # Clean up
    del inventory_data.hosts[host_name]
    del inventory_data.groups[group_name]
    if localhost_name in inventory_data.hosts:
        del inventory_data.hosts[localhost_name]
    if duplicate_localhost_name in inventory_data.hosts:
        del inventory_data.hosts[duplicate_localhost_name]
