# file mimesis/providers/address.py:137-142
# lines [137, 142]
# branches []

import pytest
from mimesis.providers.address import Address
from unittest.mock import patch

@pytest.fixture
def address_provider():
    return Address()

def test_province(address_provider):
    # Mock the state method to return a consistent value
    with patch.object(Address, 'state', return_value='MockState'):
        province = address_provider.province()
        assert province is not None
        assert isinstance(province, str)
        # Since province is an alias for state, we expect the same result
        state = address_provider.state()
        assert province == state
