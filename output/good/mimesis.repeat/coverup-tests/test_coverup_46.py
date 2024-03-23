# file mimesis/providers/payment.py:135-148
# lines [135, 136, 146, 147, 148]
# branches []

import pytest
from mimesis.providers.payment import Payment
from unittest.mock import patch

@pytest.fixture
def payment_provider():
    return Payment()

def test_credit_card_expiration_date(payment_provider):
    with patch.object(payment_provider.random, 'randint', side_effect=[3, 19]):
        expiration_date = payment_provider.credit_card_expiration_date()
        assert expiration_date == '03/19'

    with patch.object(payment_provider.random, 'randint', side_effect=[12, 25]):
        expiration_date = payment_provider.credit_card_expiration_date()
        assert expiration_date == '12/25'

    with patch.object(payment_provider.random, 'randint', side_effect=[1, 16]):
        expiration_date = payment_provider.credit_card_expiration_date()
        assert expiration_date == '01/16'

    with patch.object(payment_provider.random, 'randint', side_effect=[6, 22]):
        expiration_date = payment_provider.credit_card_expiration_date(minimum=20, maximum=30)
        assert expiration_date == '06/22'
