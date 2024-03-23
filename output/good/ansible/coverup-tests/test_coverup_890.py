# file lib/ansible/inventory/host.py:54-55
# lines [54, 55]
# branches []

import pytest
from ansible.inventory.host import Host

# Mock class to simulate the Host class behavior
class MockHost(Host):
    def get_name(self):
        return "mockhost"

# Test function to cover __repr__ method in Host class
def test_host_repr():
    host = MockHost()
    assert repr(host) == "mockhost", "The __repr__ method should return the result of get_name()"
