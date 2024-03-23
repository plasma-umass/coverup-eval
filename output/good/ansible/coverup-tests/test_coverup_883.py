# file lib/ansible/inventory/host.py:48-49
# lines [48, 49]
# branches []

import pytest
from ansible.inventory.host import Host

# Assuming the Host class has a 'name' attribute that can be set during initialization

@pytest.fixture
def host_cleanup():
    # Fixture to create a host and then clean up after the test
    created_hosts = []

    yield created_hosts

    # Cleanup code
    for host in created_hosts:
        del host

def test_host_hash(host_cleanup):
    # Create a host instance
    host_name = "test_host"
    host = Host(name=host_name)
    host_cleanup.append(host)

    # Test the __hash__ method
    expected_hash = hash(host_name)
    assert hash(host) == expected_hash, "Host object hash does not match expected hash"
