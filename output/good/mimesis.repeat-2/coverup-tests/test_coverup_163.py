# file mimesis/providers/address.py:82-88
# lines [87, 88]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_street_suffix(address_provider):
    # Mock the data to ensure the test hits the desired lines
    address_provider._data = {
        'street': {
            'suffix': ['Avenue', 'Boulevard', 'Court', 'Drive', 'Lane', 'Road', 'Street']
        }
    }
    
    suffix = address_provider.street_suffix()
    assert suffix in address_provider._data['street']['suffix']
