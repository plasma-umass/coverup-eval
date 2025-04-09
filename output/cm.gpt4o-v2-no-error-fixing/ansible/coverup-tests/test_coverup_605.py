# file: lib/ansible/inventory/host.py:45-46
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest
from ansible.inventory.host import Host

def test_host_ne():
    host1 = Host(name="host1")
    host2 = Host(name="host2")

    # Ensure that host1 and host2 are not equal
    assert host1 != host2

    # Ensure that host1 is equal to itself
    assert not (host1 != host1)

    # Create a mock object that is not an instance of Host
    class MockHost:
        pass

    mock_host = MockHost()

    # Ensure that host1 is not equal to an instance of a different class
    assert host1 != mock_host
