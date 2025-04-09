# file mimesis/providers/address.py:200-206
# lines [205, 206]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_city(address_provider, mocker):
    # Mock the '_data' attribute of the Address provider to contain a 'city' key with a list.
    mocker.patch.object(address_provider, '_data', {'city': ['New York', 'Los Angeles', 'Chicago']})
    
    # Now, when we call the 'city' method, it should return a city from the list
    city = address_provider.city()
    assert city in address_provider._data['city']
