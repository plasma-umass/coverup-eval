# file mimesis/providers/address.py:82-88
# lines [87, 88]
# branches []

import pytest
from mimesis.providers.address import Address
from unittest.mock import patch

@pytest.fixture
def address():
    return Address()

def test_street_suffix(address):
    mock_data = {'street': {'suffix': ['Avenue', 'Boulevard', 'Court']}}
    with patch.object(address, '_data', mock_data):
        suffix = address.street_suffix()
        assert suffix in mock_data['street']['suffix']
