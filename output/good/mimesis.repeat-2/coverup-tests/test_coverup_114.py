# file mimesis/providers/address.py:200-206
# lines [200, 205, 206]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_city(address_provider):
    city = address_provider.city()
    assert city in address_provider._data['city']
