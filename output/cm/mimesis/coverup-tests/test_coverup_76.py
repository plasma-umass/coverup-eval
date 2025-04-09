# file mimesis/providers/payment.py:70-83
# lines [70, 81, 82, 83]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.random import Random

def test_ethereum_address(mocker):
    # Mock the getrandbits method to return a known value
    mocker.patch.object(Random, 'getrandbits', return_value=0x1234567890ABCDEF1234567890ABCDEF12345678)

    payment = Payment()
    address = payment.ethereum_address()

    # Assert that the address starts with '0x' and is 42 characters long (2 characters for '0x' and 40 for the address)
    assert address.startswith('0x')
    assert len(address) == 42

    # Assert that the address is the correct one based on the mocked getrandbits value
    expected_address = '0x1234567890abcdef1234567890abcdef12345678'
    assert address == expected_address
