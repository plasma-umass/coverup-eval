# file mimesis/providers/address.py:137-142
# lines [137, 142]
# branches []

import pytest
from mimesis.providers.address import Address

def test_province_method(mocker):
    address = Address()
    
    # Mock the state method to ensure it is called and returns a specific value
    mock_state = mocker.patch.object(address, 'state', return_value='Mocked State')
    
    # Call the province method
    result = address.province()
    
    # Assert that the state method was called
    mock_state.assert_called_once()
    
    # Assert that the result of province is the same as the mocked state method
    assert result == 'Mocked State'
