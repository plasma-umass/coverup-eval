# file lib/ansible/inventory/group.py:260-264
# lines [260, 262, 263, 264]
# branches ['262->263', '262->264']

import pytest
from ansible.inventory.group import Group

# Mock class to simulate the behavior of the actual class that Group would interact with
class MockedHosts:
    def __init__(self, hosts):
        self.hosts = hosts

    def _get_hosts(self):
        return self.hosts

@pytest.fixture
def group_with_mocked_hosts(mocker):
    group = Group()
    mocked_hosts = MockedHosts(['host1', 'host2'])
    mocker.patch.object(group, '_get_hosts', return_value=mocked_hosts._get_hosts())
    return group

def test_get_hosts_caching(group_with_mocked_hosts):
    # Call get_hosts twice to test caching
    hosts_first_call = group_with_mocked_hosts.get_hosts()
    hosts_second_call = group_with_mocked_hosts.get_hosts()

    # Assert that the same list object is returned, indicating caching
    assert hosts_first_call is hosts_second_call

    # Assert that the list contains the correct hosts
    assert hosts_first_call == ['host1', 'host2']
