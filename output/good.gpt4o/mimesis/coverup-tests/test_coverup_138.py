# file mimesis/providers/payment.py:85-93
# lines [85, 93]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.data import CREDIT_CARD_NETWORKS

@pytest.fixture
def payment_provider():
    return Payment()

def test_credit_card_network(payment_provider):
    network = payment_provider.credit_card_network()
    assert network in CREDIT_CARD_NETWORKS
