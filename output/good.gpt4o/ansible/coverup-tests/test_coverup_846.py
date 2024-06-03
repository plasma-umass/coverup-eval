# file lib/ansible/inventory/host.py:150-151
# lines [150, 151]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Host class is defined in ansible.inventory.host
from ansible.inventory.host import Host

@pytest.fixture
def host():
    # Create a Host instance with a mock 'groups' attribute
    host = Host()
    host.groups = MagicMock()
    return host

def test_get_groups(host):
    # Call the get_groups method
    groups = host.get_groups()
    
    # Assert that the returned value is the mock object
    assert groups == host.groups
