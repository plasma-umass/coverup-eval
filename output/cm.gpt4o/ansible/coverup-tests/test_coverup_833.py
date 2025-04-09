# file lib/ansible/inventory/host.py:48-49
# lines [48, 49]
# branches []

import pytest

# Assuming the Host class is imported from ansible.inventory.host
from ansible.inventory.host import Host

def test_host_hash():
    # Create an instance of the Host class
    host_instance = Host()
    host_instance.name = "test_host"

    # Calculate the hash
    host_hash = hash(host_instance)

    # Verify the hash is as expected
    assert host_hash == hash("test_host")
