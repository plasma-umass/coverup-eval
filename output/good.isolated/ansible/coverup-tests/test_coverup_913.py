# file lib/ansible/inventory/host.py:45-46
# lines [45, 46]
# branches []

import pytest
from ansible.inventory.host import Host

# Assuming the Host class has an __eq__ method defined elsewhere
# and that it correctly compares hosts based on their 'name' attribute

class MockedHost(Host):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, MockedHost):
            return self.name == other.name
        return False

def test_host_ne_method():
    host1 = MockedHost(name='host1')
    host2 = MockedHost(name='host2')
    host3 = MockedHost(name='host1')

    # Test inequality
    assert host1 != host2, "Hosts with different names should not be equal"

    # Test equality
    assert not (host1 != host3), "Hosts with the same name should be equal"

    # Cleanup is not necessary here as we are not modifying any shared state
