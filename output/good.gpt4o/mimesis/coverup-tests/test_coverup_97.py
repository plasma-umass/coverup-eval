# file mimesis/providers/address.py:158-164
# lines [158, 163, 164]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis import Generic

@pytest.fixture
def address_provider():
    generic = Generic('en')
    return generic.address

def test_postal_code(address_provider):
    postal_code = address_provider.postal_code()
    assert isinstance(postal_code, str)
    assert len(postal_code) > 0

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
