# file mimesis/providers/address.py:166-173
# lines [173]
# branches []

import pytest
from mimesis.providers.address import Address
from unittest.mock import patch


@pytest.fixture
def address():
    return Address('en')


def test_zip_code(address):
    with patch.object(Address, 'postal_code', return_value='12345') as mock_postal_code:
        zip_code = address.zip_code()
        assert mock_postal_code.called
        assert zip_code == '12345', "zip_code should be an alias for postal_code"
