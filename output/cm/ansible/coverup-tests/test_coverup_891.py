# file lib/ansible/inventory/host.py:29-33
# lines [29, 30]
# branches []

import pytest
from ansible.inventory.host import Host

# Assuming the Host class has more to it than shown in the snippet
# and that it has some sort of cleanup or reset mechanism

def test_host_creation():
    # Test creation of Host instance
    host = Host(name='testhost')
    assert host.name == 'testhost', "Host name should be set correctly"
    assert isinstance(host.vars, dict), "Host vars should be a dictionary"
    assert isinstance(host.groups, list), "Host groups should be a list"

    # Cleanup
    # Assuming Host does not affect global state and does not need explicit cleanup
