# file lib/ansible/inventory/host.py:51-52
# lines [51, 52]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Host class is imported from ansible.inventory.host
from ansible.inventory.host import Host

def test_host_str_method(mocker):
    # Create a mock for the get_name method
    mock_get_name = mocker.patch.object(Host, 'get_name', return_value='test_host')

    # Instantiate the Host object
    host = Host()

    # Call the __str__ method and assert the result
    assert str(host) == 'test_host'

    # Verify that get_name was called exactly once
    mock_get_name.assert_called_once()
