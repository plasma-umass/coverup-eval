# file mimesis/providers/address.py:74-80
# lines [74, 79, 80]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address_provider():
    generic = Generic('en')
    return generic.address

def test_street_name(address_provider):
    street_name = address_provider.street_name()
    assert isinstance(street_name, str)
    assert street_name in address_provider._data['street']['name']
