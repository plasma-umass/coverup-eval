# file: lib/ansible/inventory/host.py:48-49
# asked: {"lines": [48, 49], "branches": []}
# gained: {"lines": [48, 49], "branches": []}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test_host")

def test_host_hash(host):
    # Ensure the hash function works as expected
    assert hash(host) == hash("test_host")

def test_host_hash_different_name():
    # Ensure the hash function works with a different name
    host = Host(name="another_host")
    assert hash(host) == hash("another_host")
