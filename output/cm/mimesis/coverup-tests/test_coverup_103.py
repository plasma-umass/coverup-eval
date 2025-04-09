# file mimesis/providers/address.py:121-128
# lines [121, 127, 128]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_state_with_abbr(address_provider):
    state_abbr = address_provider.state(abbr=True)
    assert state_abbr.isupper() and len(state_abbr) == 2

def test_state_without_abbr(address_provider):
    state_name = address_provider.state(abbr=False)
    assert isinstance(state_name, str) and len(state_name) > 2

def test_state_default_abbr(address_provider):
    state_default = address_provider.state()
    assert isinstance(state_default, str)
