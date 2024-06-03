# file mimesis/providers/address.py:262-267
# lines [262, 267]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.data import CALLING_CODES

@pytest.fixture
def address_provider():
    return Address()

def test_calling_code(address_provider):
    calling_code = address_provider.calling_code()
    assert calling_code in CALLING_CODES
