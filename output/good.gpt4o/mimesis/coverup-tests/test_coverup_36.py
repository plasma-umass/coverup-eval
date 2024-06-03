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

def test_country_with_random(address_provider, mocker):
    # Mock the random choice method to return a specific value
    mocker.patch.object(address_provider.random, 'choice', return_value='Random Country')
    
    result = address_provider.country(allow_random=True)
    assert result == 'Random Country'

def test_country_without_random(address_provider):
    # Assuming the current locale country is 'United States' for the 'en' locale
    result = address_provider.country(allow_random=False)
    assert result == address_provider._data['country']['current_locale']
