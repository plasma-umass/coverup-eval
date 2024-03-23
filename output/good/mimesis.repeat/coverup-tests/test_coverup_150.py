# file mimesis/providers/address.py:158-164
# lines [158, 163, 164]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address_provider():
    return Address('en')

def test_postal_code(address_provider):
    postal_code = address_provider.postal_code()
    assert postal_code is not None
    assert isinstance(postal_code, str)
    assert len(postal_code) > 0

    # Check if the postal code matches the format for the locale
    generic = Generic('en')
    postal_code_fmt = generic.address._data['postal_code_fmt']
    assert any(char.isdigit() for char in postal_code) == any(char == "#" for char in postal_code_fmt)
