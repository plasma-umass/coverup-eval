# file mimesis/providers/address.py:189-198
# lines [196]
# branches ['195->196']

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address_provider():
    generic = Generic('en')
    return generic.address

def test_country_with_allow_random(address_provider, mocker):
    # Mock the random.choice method to return a specific value
    mocker.patch.object(address_provider.random, 'choice', return_value='MockCountry')

    # Call the method with allow_random set to True
    result = address_provider.country(allow_random=True)

    # Assert that the mocked method was called
    address_provider.random.choice.assert_called_once()

    # Assert that the result is the mocked value
    assert result == 'MockCountry'

def test_country_without_allow_random(address_provider):
    # Call the method with allow_random set to False
    result = address_provider.country(allow_random=False)

    # Assert that the result is the current locale's country
    assert result == address_provider._data['country']['current_locale']
