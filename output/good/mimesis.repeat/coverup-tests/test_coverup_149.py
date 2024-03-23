# file mimesis/providers/address.py:200-206
# lines [200, 205, 206]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address_provider():
    generic = Generic()
    return Address(generic.locale)

def test_city(address_provider, mocker):
    # Mock the data to control the output
    mocker.patch.object(
        address_provider, '_data', 
        {'city': ['New York', 'Los Angeles', 'Chicago']}
    )
    
    # Call the method to test
    city = address_provider.city()
    
    # Assert that the result is one of the cities in the mocked data
    assert city in ['New York', 'Los Angeles', 'Chicago']
