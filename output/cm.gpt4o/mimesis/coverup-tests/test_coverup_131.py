# file mimesis/providers/address.py:130-135
# lines [130, 135]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_region_method(address_provider, mocker):
    # Mock the state method to ensure it gets called
    mock_state = mocker.patch.object(address_provider, 'state', return_value='Mocked State')
    
    # Call the region method
    result = address_provider.region()
    
    # Assert that the state method was called
    mock_state.assert_called_once()
    
    # Assert that the result is as expected
    assert result == 'Mocked State'
