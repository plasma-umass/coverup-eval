# file mimesis/providers/address.py:240-249
# lines [240, 246, 247, 248]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_coordinates_default(address_provider):
    coords = address_provider.coordinates()
    assert 'longitude' in coords
    assert 'latitude' in coords
    assert isinstance(coords['longitude'], float)
    assert isinstance(coords['latitude'], float)

def test_coordinates_dms(address_provider):
    coords = address_provider.coordinates(dms=True)
    assert 'longitude' in coords
    assert 'latitude' in coords
    assert isinstance(coords['longitude'], str)
    assert isinstance(coords['latitude'], str)
    assert 'º' in coords['longitude']
    assert 'º' in coords['latitude']
