# file mimesis/providers/address.py:74-80
# lines [74, 79, 80]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_street_name(address_provider, mocker):
    # Mock the data to ensure the test is predictable
    mocker.patch.object(
        address_provider, '_data',
        {'street': {'name': ['Mock Street', 'Example Avenue']}}
    )
    
    # Call the method to test
    street_name = address_provider.street_name()
    
    # Assert that the result is in the mocked data
    assert street_name in ['Mock Street', 'Example Avenue']

    # Clean up is handled by the mocker fixture, no action required
