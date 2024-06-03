# file mimesis/providers/address.py:166-173
# lines [166, 173]
# branches []

import pytest
from mimesis.providers.address import Address

def test_zip_code(mocker):
    address = Address()
    
    # Mock the postal_code method to ensure it gets called
    mock_postal_code = mocker.patch.object(address, 'postal_code', return_value='12345')
    
    # Call the zip_code method
    result = address.zip_code()
    
    # Assert that postal_code was called once
    mock_postal_code.assert_called_once()
    
    # Assert that the result is as expected
    assert result == '12345'
