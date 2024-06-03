# file lib/ansible/inventory/host.py:54-55
# lines [54, 55]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Host class is imported from ansible.inventory.host
from ansible.inventory.host import Host

def test_host_repr(mocker):
    # Mock the get_name method
    mock_get_name = mocker.patch.object(Host, 'get_name', return_value='test_host')

    # Create an instance of Host
    host = Host()

    # Call __repr__ and check the result
    assert repr(host) == 'test_host'

    # Verify that get_name was called exactly once
    mock_get_name.assert_called_once()

