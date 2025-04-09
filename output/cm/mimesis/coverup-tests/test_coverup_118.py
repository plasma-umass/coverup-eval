# file mimesis/providers/address.py:74-80
# lines [74, 79, 80]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_street_name(address_provider, mocker):
    # Mock the data to control the output
    fake_data = {
        'street': {
            'name': ['Mockingbird Lane', 'Elm Street', 'Baker Street']
        }
    }
    
    # Patch the _data attribute of the address_provider instance
    mocker.patch.object(address_provider, '_data', fake_data)
    
    # Call the method to test
    street_name = address_provider.street_name()
    
    # Assert that the result is in the mocked data
    assert street_name in fake_data['street']['name']
