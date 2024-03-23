# file lib/ansible/inventory/host.py:102-103
# lines [102, 103]
# branches []

import pytest
from ansible.inventory.host import Host

# Assuming the Host class has a constructor that accepts a name
# If not, the test should be adjusted according to the actual Host class implementation

def test_host_get_name(mocker):
    # Setup
    host_name = "test_host"
    host = Host(name=host_name)

    # Exercise
    result = host.get_name()

    # Verify
    assert result == host_name

    # Cleanup - nothing to clean up as no external resources are being used
