# file mimesis/providers/address.py:262-267
# lines [262, 267]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.data import CALLING_CODES

def test_calling_code(mocker):
    # Mock the random.choice method to return a specific calling code
    mocker.patch(
        'mimesis.random.Random.choice',
        return_value='+1'
    )

    address = Address()

    # Call the method
    result = address.calling_code()

    # Check that the result is in the CALLING_CODES list
    assert result in CALLING_CODES
    # Check that the result is the one we mocked
    assert result == '+1'
