# file mimesis/providers/payment.py:57-68
# lines [57, 65, 66, 67, 68]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.random import Random
from unittest.mock import patch

@pytest.fixture
def payment_provider():
    return Payment(Random())

def test_bitcoin_address(payment_provider):
    with patch.object(payment_provider.random, 'choice') as mock_choice:
        mock_choice.side_effect = ['1'] + ['a' for _ in range(33)]
        bitcoin_address = payment_provider.bitcoin_address()
        assert bitcoin_address.startswith('1')
        assert len(bitcoin_address) == 34

        mock_choice.side_effect = ['3'] + ['a' for _ in range(33)]
        bitcoin_address = payment_provider.bitcoin_address()
        assert bitcoin_address.startswith('3')
        assert len(bitcoin_address) == 34
