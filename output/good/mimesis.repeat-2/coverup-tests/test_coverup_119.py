# file mimesis/providers/address.py:232-238
# lines [232, 238]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_longitude_dms_format(address_provider):
    # Test the longitude method with dms format enabled
    longitude_dms = address_provider.longitude(dms=True)
    assert isinstance(longitude_dms, str), "Longitude in DMS format should be a string"

def test_longitude_float_format(address_provider):
    # Test the longitude method with dms format disabled
    longitude_float = address_provider.longitude(dms=False)
    assert isinstance(longitude_float, float), "Longitude in float format should be a float"
