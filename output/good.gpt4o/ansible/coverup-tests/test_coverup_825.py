# file lib/ansible/inventory/host.py:161-162
# lines [161, 162]
# branches []

import pytest
from unittest.mock import patch

# Assuming combine_vars is a function in the ansible.inventory.host module
from ansible.inventory.host import Host, combine_vars

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.inventory.host.combine_vars')

def test_get_vars(mock_combine_vars):
    # Arrange
    host = Host()
    host.vars = {'var1': 'value1'}
    magic_vars = {'magic_var1': 'magic_value1'}
    
    # Mock the get_magic_vars method to return predefined magic_vars
    with patch.object(Host, 'get_magic_vars', return_value=magic_vars):
        # Act
        result = host.get_vars()
        
        # Assert
        mock_combine_vars.assert_called_once_with(host.vars, magic_vars)
        assert result == mock_combine_vars.return_value
