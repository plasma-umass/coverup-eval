# file mimesis/providers/address.py:137-142
# lines [137, 142]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_province(address_provider):
    province = address_provider.province()
    assert province is not None
    assert isinstance(province, str)
    # Ensure province is one of the expected provinces from the data set
    assert province in address_provider._data['state']['name']
