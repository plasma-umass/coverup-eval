# file: lib/ansible/inventory/host.py:48-49
# asked: {"lines": [48, 49], "branches": []}
# gained: {"lines": [48, 49], "branches": []}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host_instance():
    return Host(name="test_host")

def test_host_hash(host_instance):
    # Ensure the __hash__ method is called and the correct hash is returned
    host_hash = hash(host_instance)
    expected_hash = hash("test_host")
    assert host_hash == expected_hash

    # Clean up
    del host_instance
