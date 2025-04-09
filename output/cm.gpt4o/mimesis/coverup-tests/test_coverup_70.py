# file mimesis/providers/address.py:30-37
# lines [30, 35, 36, 37]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

def test_address_initialization(mocker):
    # Mock the _pull method to avoid actual file operations
    mock_pull = mocker.patch.object(Address, '_pull', autospec=True)

    # Create an instance of Address
    address = Address(locale='en')

    # Assert that the _datafile attribute is set correctly
    assert address._datafile == 'address.json'

    # Assert that the _pull method was called with the correct argument
    mock_pull.assert_called_once_with('address.json')

    # Clean up by deleting the created instance
    del address
