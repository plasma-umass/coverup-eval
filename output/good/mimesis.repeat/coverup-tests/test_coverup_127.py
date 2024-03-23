# file mimesis/providers/address.py:144-149
# lines [144, 149]
# branches []

import pytest
from mimesis.providers.address import Address

@pytest.fixture
def address_provider():
    return Address()

def test_federal_subject(address_provider):
    # Call the federal_subject method to ensure it uses the state method
    result = address_provider.federal_subject()
    # Assert that the result is not empty, since state should return a non-empty string
    assert result != ""
