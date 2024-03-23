# file mimesis/providers/address.py:158-164
# lines [158, 163, 164]
# branches []

import pytest
from mimesis import Address

@pytest.fixture
def address_provider():
    return Address()

def test_postal_code(address_provider):
    postal_code = address_provider.postal_code()
    assert postal_code is not None
    assert isinstance(postal_code, str)
    assert len(postal_code) > 0
    assert any(char.isdigit() for char in postal_code)
