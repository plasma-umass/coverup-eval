# file mimesis/providers/payment.py:47-55
# lines [47, 55]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person
from unittest.mock import patch

@pytest.fixture
def payment_provider():
    return Payment()

def test_paypal(payment_provider):
    with patch.object(Person, 'email', return_value='test@example.com'):
        email = payment_provider.paypal()
        assert email == 'test@example.com'
