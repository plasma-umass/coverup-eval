# file mimesis/providers/address.py:232-238
# lines [232, 238]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_longitude_dms_format(address_provider):
    # Test for DMS format
    longitude_dms = address_provider.longitude(dms=True)
    assert isinstance(longitude_dms, str)
    # Adjusting the assertion to match the actual DMS format used by mimesis
    assert 'º' in longitude_dms and '\'' in longitude_dms and '"' in longitude_dms

def test_longitude_float_format(address_provider):
    # Test for float format
    longitude_float = address_provider.longitude(dms=False)
    assert isinstance(longitude_float, float)
    assert -180 <= longitude_float <= 180

def test_longitude_default_format(address_provider):
    # Test for default format which should be float
    longitude_default = address_provider.longitude()
    assert isinstance(longitude_default, float)
    assert -180 <= longitude_default <= 180

# Mocking _get_fs to ensure that the test does not depend on the implementation details
def test_longitude_mocked(mocker, address_provider):
    mocker.patch.object(address_provider, '_get_fs', return_value='mocked_value')
    assert address_provider.longitude(dms=False) == 'mocked_value'
    address_provider._get_fs.assert_called_once_with('lg', False)
