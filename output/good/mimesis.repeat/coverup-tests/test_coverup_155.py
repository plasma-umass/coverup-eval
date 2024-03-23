# file mimesis/providers/address.py:224-230
# lines [224, 230]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_latitude_dms_format(address_provider, mocker):
    # Mock the _get_fs method to control its output
    mocker.patch.object(
        address_provider, '_get_fs', return_value='51°28′40″N'
    )
    
    # Call the method with dms=True to test the DMS format branch
    result = address_provider.latitude(dms=True)
    
    # Assert that the mocked _get_fs method was called with the correct parameters
    address_provider._get_fs.assert_called_once_with('lt', True)
    
    # Assert that the result is a string, as expected for DMS format
    assert isinstance(result, str)
    assert result == '51°28′40″N'

def test_latitude_decimal_format(address_provider, mocker):
    # Mock the _get_fs method to control its output
    mocker.patch.object(
        address_provider, '_get_fs', return_value=51.4778
    )
    
    # Call the method with dms=False to test the decimal format branch
    result = address_provider.latitude(dms=False)
    
    # Assert that the mocked _get_fs method was called with the correct parameters
    address_provider._get_fs.assert_called_once_with('lt', False)
    
    # Assert that the result is a float, as expected for decimal format
    assert isinstance(result, float)
    assert result == 51.4778
