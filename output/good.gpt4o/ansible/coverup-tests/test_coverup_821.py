# file lib/ansible/inventory/host.py:29-33
# lines [29, 30]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Host class is defined in ansible/inventory/host.py
from ansible.inventory.host import Host

@pytest.fixture
def mock_host():
    with patch('ansible.inventory.host.Host') as MockHost:
        yield MockHost

def test_host_initialization(mock_host):
    # Create an instance of the Host class
    host_instance = Host()
    
    # Verify that the instance is created
    assert isinstance(host_instance, Host)
    
    # Verify that the default attributes are set correctly
    assert hasattr(host_instance, 'name')
    assert hasattr(host_instance, 'vars')
    assert hasattr(host_instance, 'groups')

    # Clean up
    del host_instance
