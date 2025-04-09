# file mimesis/providers/address.py:232-238
# lines [232, 238]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_longitude_float(address_provider):
    longitude = address_provider.longitude(dms=False)
    assert isinstance(longitude, float), "Longitude should be a float when dms is False"

def test_longitude_dms(address_provider):
    longitude = address_provider.longitude(dms=True)
    assert isinstance(longitude, str), "Longitude should be a string when dms is True"
    assert 'º' in longitude or '°' in longitude, "Longitude in DMS format should contain degrees symbol"

# Clean up is not necessary in this case as no external state is modified
