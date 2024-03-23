# file mimesis/providers/address.py:224-230
# lines [224, 230]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address():
    return Address()

def test_latitude_dms_format(address):
    # Test the latitude method with dms format
    latitude_dms = address.latitude(dms=True)
    assert isinstance(latitude_dms, str)
    assert '°' in latitude_dms or 'º' in latitude_dms
    assert "'" in latitude_dms
    assert '"' in latitude_dms or 'N' in latitude_dms or 'S' in latitude_dms

def test_latitude_float_format(address):
    # Test the latitude method with float format
    latitude_float = address.latitude(dms=False)
    assert isinstance(latitude_float, float)
    assert -90 <= latitude_float <= 90

def test_latitude_default_format(address):
    # Test the latitude method with default format
    latitude_default = address.latitude()
    assert isinstance(latitude_default, float)
    assert -90 <= latitude_default <= 90

def test_latitude_with_mocked_fs(mocker, address):
    # Mock the _get_fs method to ensure it is called with correct parameters
    mock_get_fs = mocker.patch.object(address, '_get_fs', return_value='mocked_value')
    result = address.latitude(dms=True)
    mock_get_fs.assert_called_once_with('lt', True)
    assert result == 'mocked_value'

    mock_get_fs.reset_mock()
    result = address.latitude(dms=False)
    mock_get_fs.assert_called_once_with('lt', False)
    assert result == 'mocked_value'
