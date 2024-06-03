# file mimesis/providers/payment.py:20-22
# lines [20, 21]
# branches []

import pytest
from mimesis.providers.payment import Payment

@pytest.fixture
def payment_provider():
    return Payment()

def test_payment_provider(payment_provider):
    assert payment_provider is not None
    assert isinstance(payment_provider, Payment)
