# file mimesis/providers/address.py:240-249
# lines [240, 246, 247, 248]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_coordinates_dms_format(address_provider):
    # Test the coordinates method with dms parameter set to True
    coords_dms = address_provider.coordinates(dms=True)
    assert isinstance(coords_dms, dict)
    assert 'longitude' in coords_dms
    assert 'latitude' in coords_dms
    # Since we don't know the internal implementation of _get_fs,
    # we can't assert the exact format of the coordinates, but we can check the type
    assert isinstance(coords_dms['longitude'], str)
    assert isinstance(coords_dms['latitude'], str)

def test_coordinates_decimal_format(address_provider):
    # Test the coordinates method with dms parameter set to False
    coords_decimal = address_provider.coordinates(dms=False)
    assert isinstance(coords_decimal, dict)
    assert 'longitude' in coords_decimal
    assert 'latitude' in coords_decimal
    # Since we don't know the internal implementation of _get_fs,
    # we can't assert the exact format of the coordinates, but we can check the type
    assert isinstance(coords_decimal['longitude'], (float, int))
    assert isinstance(coords_decimal['latitude'], (float, int))
