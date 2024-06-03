# file mimesis/providers/address.py:66-72
# lines [66, 72]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_street_number_default(address_provider):
    street_number = address_provider.street_number()
    assert 1 <= int(street_number) <= 1400

def test_street_number_custom_max(address_provider):
    custom_max = 500
    street_number = address_provider.street_number(maximum=custom_max)
    assert 1 <= int(street_number) <= custom_max
