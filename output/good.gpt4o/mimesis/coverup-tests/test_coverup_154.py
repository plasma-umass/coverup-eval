# file mimesis/providers/address.py:224-230
# lines [224, 230]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_latitude_float(address_provider):
    latitude = address_provider.latitude(dms=False)
    assert isinstance(latitude, float)
    assert -90.0 <= latitude <= 90.0

def test_latitude_dms(address_provider):
    latitude = address_provider.latitude(dms=True)
    assert isinstance(latitude, str)
    assert 'º' in latitude
    assert '\'' in latitude
    assert '"' in latitude
