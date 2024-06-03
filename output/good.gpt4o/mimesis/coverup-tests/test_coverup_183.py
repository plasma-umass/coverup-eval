# file mimesis/providers/address.py:121-128
# lines [127, 128]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_state_full_name(address_provider):
    state_name = address_provider.state(abbr=False)
    assert isinstance(state_name, str)
    assert len(state_name) > 0

def test_state_abbr(address_provider):
    state_abbr = address_provider.state(abbr=True)
    assert isinstance(state_abbr, str)
    assert len(state_abbr) > 0
