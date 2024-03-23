# file mimesis/providers/address.py:262-267
# lines [267]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.data import CALLING_CODES

def test_calling_code(mocker):
    # Mock the random.choice method to ensure the test is deterministic
    mocker.patch(
        'mimesis.random.Random.choice',
        return_value=CALLING_CODES[0]
    )

    address = Address()
    calling_code = address.calling_code()

    # Assert that the calling code is in the list of CALLING_CODES
    assert calling_code in CALLING_CODES
    # Assert that the mock was called, ensuring the line is executed
    address.random.choice.assert_called_once_with(CALLING_CODES)
