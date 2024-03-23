# file mimesis/providers/payment.py:85-93
# lines [93]
# branches []

import pytest
from mimesis.providers.payment import Payment

# Since the actual CREDIT_CARD_NETWORKS is not available, we will mock it.
# The test error indicates that 'Chase' is a possible value, so we include it in our mock.
MOCKED_CREDIT_CARD_NETWORKS = ['Visa', 'MasterCard', 'American Express', 'Discover', 'Chase']

@pytest.fixture
def payment_provider(mocker):
    mocker.patch('mimesis.providers.payment.CREDIT_CARD_NETWORKS', MOCKED_CREDIT_CARD_NETWORKS)
    return Payment()

def test_credit_card_network(payment_provider):
    network = payment_provider.credit_card_network()
    assert network in MOCKED_CREDIT_CARD_NETWORKS
