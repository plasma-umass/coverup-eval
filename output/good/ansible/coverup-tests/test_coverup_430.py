# file lib/ansible/inventory/data.py:236-243
# lines [236, 238, 239, 241, 242, 243]
# branches ['238->239', '238->241', '241->exit', '241->242']

import pytest
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.inventory.group import Group

class TestInventoryData:

    @pytest.fixture
    def inventory_data(self):
        return InventoryData()

    @pytest.fixture
    def host(self):
        return Host(name='testhost')

    @pytest.fixture
    def group(self):
        return Group(name='testgroup')

    def test_remove_host(self, inventory_data, host, group, mocker):
        # Setup the inventory with a host and a group containing the host
        inventory_data.hosts[host.name] = host
        inventory_data.groups[group.name] = group
        group.add_host(host)

        # Ensure the host is in the inventory and the group
        assert host.name in inventory_data.hosts
        assert host in group.get_hosts()

        # Mock the remove_host method of the group to ensure it's called
        mocker.patch.object(group, 'remove_host')

        # Perform the removal
        inventory_data.remove_host(host)

        # Assert the host is removed from the inventory
        assert host.name not in inventory_data.hosts

        # Assert the remove_host method of the group was called
        group.remove_host.assert_called_once_with(host)

        # Cleanup
        if host.name in inventory_data.hosts:
            del inventory_data.hosts[host.name]
        if group.name in inventory_data.groups:
            del inventory_data.groups[group.name]
