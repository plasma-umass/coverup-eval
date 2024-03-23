# file mimesis/providers/address.py:166-173
# lines [166, 173]
# branches []

import pytest
from mimesis.providers.address import Address
from unittest.mock import patch

@pytest.fixture
def address_provider():
    return Address()

def test_zip_code(address_provider):
    with patch.object(Address, 'postal_code', return_value='12345') as mock_postal_code:
        zip_code = address_provider.zip_code()
        assert zip_code == '12345'
        mock_postal_code.assert_called_once()
