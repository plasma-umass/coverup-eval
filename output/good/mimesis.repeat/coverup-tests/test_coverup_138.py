# file mimesis/providers/address.py:130-135
# lines [130, 135]
# branches []

import pytest
from mimesis.providers.address import Address
from unittest.mock import patch

@pytest.fixture
def address_provider():
    return Address()

def test_region(address_provider):
    # Mock the state method to ensure it is being called
    with patch.object(address_provider, 'state') as mock_state:
        mock_state.return_value = 'Mocked State'
        # Call the region method which should call the state method
        result = address_provider.region()
        # Check if the state method was called
        mock_state.assert_called_once()
        # Assert that the result of region is the same as the mock return value
        assert result == 'Mocked State'
