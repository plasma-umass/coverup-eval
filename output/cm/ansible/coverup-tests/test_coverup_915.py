# file lib/ansible/inventory/host.py:51-52
# lines [51, 52]
# branches []

import pytest
from ansible.inventory.host import Host

# Assuming the Host class has a get_name method that we need to mock
# and that the Host class is part of a larger Ansible codebase.

def test_host_str_method(mocker):
    # Create a mock Host object
    mock_host = mocker.MagicMock(spec=Host)
    # Set up the return value for the get_name method
    mock_host.get_name.return_value = 'test_host'
    
    # Patch the get_name method of the Host class
    mocker.patch.object(Host, 'get_name', return_value='test_host')
    
    # Create a Host instance
    host_instance = Host()
    
    # Assert that calling str on our host instance returns the correct name
    assert str(host_instance) == 'test_host'
    # Verify that get_name was called once as a result of calling __str__
    Host.get_name.assert_called_once()
