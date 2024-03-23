# file mimesis/providers/address.py:137-142
# lines [137, 142]
# branches []

import pytest
from mimesis import Generic

@pytest.fixture
def address_provider():
    generic = Generic('en')
    return generic.address

def test_province(address_provider):
    # Since province is an alias for state, we do not compare the values
    # as they are random. We just check if the method can be called.
    province = address_provider.province()
    assert province is not None
    assert isinstance(province, str)
