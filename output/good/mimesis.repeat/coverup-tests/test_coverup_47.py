# file mimesis/providers/address.py:189-198
# lines [189, 195, 196, 198]
# branches ['195->196', '195->198']

import pytest
from mimesis.providers.address import Address
from mimesis import Generic


@pytest.fixture
def address_provider():
    generic = Generic('en')
    return generic.address


def test_country_with_allow_random(address_provider, mocker):
    mocker.patch.object(
        address_provider.random, 'choice', return_value='Random Country'
    )
    country = address_provider.country(allow_random=True)
    assert country == 'Random Country'


def test_country_without_allow_random(address_provider):
    expected_country = address_provider._data['country']['current_locale']
    country = address_provider.country()
    assert country == expected_country
