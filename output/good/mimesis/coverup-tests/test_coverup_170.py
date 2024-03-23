# file mimesis/providers/address.py:232-238
# lines [238]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address():
    return Address()

def test_longitude_dms_format(address, mocker):
    # Mock the _get_fs method to control its output
    mocker.patch.object(
        address, '_get_fs', return_value='100°10′30″W'
    )

    # Call the longitude method with dms=True to execute the missing line
    result = address.longitude(dms=True)

    # Assert that the mocked method was called with the correct parameters
    address._get_fs.assert_called_once_with('lg', True)

    # Assert that the result is in DMS format
    assert result == '100°10′30″W', "Longitude in DMS format is not as expected"
