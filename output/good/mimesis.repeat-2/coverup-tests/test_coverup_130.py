# file mimesis/providers/address.py:144-149
# lines [144, 149]
# branches []

import pytest
from mimesis.providers.address import Address


@pytest.fixture
def address_provider():
    return Address('en')


def test_federal_subject(address_provider):
    # Test the federal_subject method to ensure it calls the state method
    # and returns the expected result.
    result = address_provider.federal_subject()
    assert result is not None
    assert isinstance(result, str)
    # Since federal_subject is an alias for state, we can check if the result
    # is in the list of states for the given locale.
    assert result in address_provider._data['state']['name']
