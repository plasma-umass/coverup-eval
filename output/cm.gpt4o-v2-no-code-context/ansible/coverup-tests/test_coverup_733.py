# file: lib/ansible/inventory/host.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming combine_vars is a function that needs to be imported
from ansible.inventory.host import Host, combine_vars

@pytest.fixture
def host():
    host = Host()
    host.vars = {'var1': 'value1'}
    host.get_magic_vars = MagicMock(return_value={'magic_var1': 'magic_value1'})
    return host

def test_get_vars(host, mocker):
    # Mock combine_vars to ensure it is called with the correct arguments
    mock_combine_vars = mocker.patch('ansible.inventory.host.combine_vars', return_value={'combined_var': 'combined_value'})
    
    result = host.get_vars()
    
    # Assert that combine_vars was called with the correct arguments
    mock_combine_vars.assert_called_once_with({'var1': 'value1'}, {'magic_var1': 'magic_value1'})
    
    # Assert that the result is as expected
    assert result == {'combined_var': 'combined_value'}
