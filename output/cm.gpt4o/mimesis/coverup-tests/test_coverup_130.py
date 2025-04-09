# file mimesis/providers/address.py:144-149
# lines [144, 149]
# branches []

import pytest
from mimesis.providers.address import Address

def test_federal_subject(mocker):
    address = Address()
    
    # Mock the state method to ensure it is called and returns a specific value
    mock_state = mocker.patch.object(address, 'state', return_value='Mocked State')
    
    result = address.federal_subject()
    
    # Assert that the state method was called
    mock_state.assert_called_once()
    
    # Assert that the result of federal_subject is the same as the mocked state method
    assert result == 'Mocked State'
