# file mimesis/providers/address.py:189-198
# lines [195, 196, 198]
# branches ['195->196', '195->198']

import pytest
from mimesis.providers.address import Address
from mimesis import Generic


@pytest.fixture
def address_provider():
    generic = Generic('en')
    return generic.address


def test_country_with_allow_random_true(address_provider, mocker):
    # Mock the random.choice method to ensure it gets called and returns a predictable value
    mocker.patch.object(address_provider.random, 'choice', return_value='Random Country')

    # Call the method with allow_random set to True
    country = address_provider.country(allow_random=True)

    # Assert that the mocked random.choice method was called with the correct argument
    address_provider.random.choice.assert_called_once_with(address_provider._data['country']['name'])

    # Assert that the returned country is the one we mocked
    assert country == 'Random Country'
