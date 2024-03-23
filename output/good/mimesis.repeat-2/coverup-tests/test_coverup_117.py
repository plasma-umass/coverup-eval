# file mimesis/providers/payment.py:37-45
# lines [37, 45]
# branches []

import pytest
from mimesis.providers.payment import Payment

@pytest.fixture
def payment_provider():
    return Payment()

def test_cid(payment_provider):
    cid = payment_provider.cid()
    assert 1000 <= cid <= 9999, "CID should be between 1000 and 9999"
