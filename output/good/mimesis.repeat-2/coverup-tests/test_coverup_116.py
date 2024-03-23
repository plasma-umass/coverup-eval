# file mimesis/providers/address.py:121-128
# lines [121, 127, 128]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_state_full_coverage(address_provider):
    # Test for full name of state
    full_state = address_provider.state(abbr=False)
    assert isinstance(full_state, str)
    assert full_state in address_provider._data['state']['name']

    # Test for abbreviation of state
    abbr_state = address_provider.state(abbr=True)
    assert isinstance(abbr_state, str)
    assert abbr_state in address_provider._data['state']['abbr']
