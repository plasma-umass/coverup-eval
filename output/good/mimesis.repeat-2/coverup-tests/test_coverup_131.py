# file mimesis/providers/address.py:130-135
# lines [130, 135]
# branches []

import pytest
from mimesis.providers.address import Address


@pytest.fixture
def address():
    return Address('en')


def test_region(address):
    region = address.region()
    assert region is not None
    assert isinstance(region, str)
    # Since region is an alias for state, we can check if it's in the list of states
    assert region in address._data['state']['name']
