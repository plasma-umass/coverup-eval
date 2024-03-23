# file lib/ansible/inventory/data.py:236-243
# lines []
# branches ['238->241']

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

    def test_remove_host_with_group_branch(self, inventory_data, host, group):
        # Setup the inventory with a host and a group containing the host
        inventory_data.hosts[host.name] = host
        inventory_data.groups[group.name] = group
        group.add_host(host)

        # Assert preconditions
        assert host.name in inventory_data.hosts
        assert host in group.get_hosts()

        # Perform the action
        inventory_data.remove_host(host)

        # Assert postconditions
        assert host.name not in inventory_data.hosts
        assert host not in group.get_hosts()

        # Clean up by removing references to the host and group
        del inventory_data.hosts
        del inventory_data.groups

    def test_remove_host_not_in_hosts_but_in_group(self, inventory_data, host, group):
        # Setup the inventory with a group containing the host, but the host is not in inventory_data.hosts
        inventory_data.groups[group.name] = group
        group.add_host(host)

        # Assert preconditions
        assert host.name not in inventory_data.hosts
        assert host in group.get_hosts()

        # Perform the action
        inventory_data.remove_host(host)

        # Assert postconditions
        assert host.name not in inventory_data.hosts
        assert host not in group.get_hosts()

        # Clean up by removing references to the host and group
        del inventory_data.groups
