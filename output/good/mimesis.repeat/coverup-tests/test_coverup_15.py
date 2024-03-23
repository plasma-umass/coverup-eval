# file mimesis/providers/address.py:208-222
# lines [208, 216, 217, 219, 220, 222]
# branches ['219->220', '219->222']

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_get_fs_lt_dms(address_provider):
    latitude_dms = address_provider._get_fs('lt', dms=True)
    assert isinstance(latitude_dms, str)
    assert any(map(lambda x: x in latitude_dms, ['N', 'S']))

def test_get_fs_lg_dms(address_provider):
    longitude_dms = address_provider._get_fs('lg', dms=True)
    assert isinstance(longitude_dms, str)
    assert any(map(lambda x: x in longitude_dms, ['E', 'W']))

def test_get_fs_lt_float(address_provider):
    latitude_float = address_provider._get_fs('lt', dms=False)
    assert isinstance(latitude_float, float)
    assert -90 <= latitude_float <= 90

def test_get_fs_lg_float(address_provider):
    longitude_float = address_provider._get_fs('lg', dms=False)
    assert isinstance(longitude_float, float)
    assert -180 <= longitude_float <= 180
