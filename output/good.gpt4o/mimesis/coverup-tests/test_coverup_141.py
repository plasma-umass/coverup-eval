# file mimesis/providers/payment.py:150-158
# lines [150, 158]
# branches []

import pytest
from mimesis.providers.payment import Payment

@pytest.fixture
def payment_provider():
    return Payment()

def test_cvv(payment_provider):
    cvv = payment_provider.cvv()
    assert 100 <= cvv <= 999
    assert isinstance(cvv, int)
