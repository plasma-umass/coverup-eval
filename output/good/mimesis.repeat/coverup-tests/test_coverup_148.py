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
    mocker.patch.object(address_provider, '_data', fake_data)

    # Call the method
    street_name = address_provider.street_name()

    # Assert that the street name is one of the mocked names
    assert street_name in fake_data['street']['name']

    # Clean up is handled by the mocker fixture, no need for additional cleanup
