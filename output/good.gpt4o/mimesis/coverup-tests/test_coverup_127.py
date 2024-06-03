# file mimesis/providers/address.py:82-88
# lines [82, 87, 88]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_street_suffix(address_provider, mocker):
    # Mock the random choice method to ensure deterministic behavior
    mocker.patch.object(address_provider.random, 'choice', return_value='Street')
    
    suffix = address_provider.street_suffix()
    
    # Assert that the suffix is a string
    assert isinstance(suffix, str)

    # Assert that the mocked method was called with the correct data
    address_provider.random.choice.assert_called_once_with(address_provider._data['street']['suffix'])
