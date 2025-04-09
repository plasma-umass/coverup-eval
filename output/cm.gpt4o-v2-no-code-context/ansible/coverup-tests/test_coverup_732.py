# file: lib/ansible/inventory/host.py:48-49
# asked: {"lines": [48, 49], "branches": []}
# gained: {"lines": [48, 49], "branches": []}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host_instance():
    return Host(name="test_host")

def test_host_hash(host_instance):
    # Ensure the __hash__ method is called and returns the expected value
    expected_hash = hash("test_host")
    assert hash(host_instance) == expected_hash

def test_host_hash_with_different_name(monkeypatch):
    # Create a different host instance with a different name
    different_host = Host(name="different_host")
    expected_hash = hash("different_host")
    assert hash(different_host) == expected_hash
