# file mimesis/providers/payment.py:57-68
# lines [57, 65, 66, 67, 68]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.random import Random

@pytest.fixture
def payment_provider():
    return Payment(Random())

def test_bitcoin_address(payment_provider):
    address = payment_provider.bitcoin_address()
    assert len(address) == 34
    assert address[0] in ['1', '3']
    for char in address[1:]:
        assert char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
