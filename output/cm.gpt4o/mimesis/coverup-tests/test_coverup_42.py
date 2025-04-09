# file mimesis/providers/payment.py:135-148
# lines [135, 136, 146, 147, 148]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis import Generic

@pytest.fixture
def payment_provider():
    generic = Generic('en')
    return generic.payment

def test_credit_card_expiration_date(payment_provider):
    # Test with default parameters
    expiration_date = payment_provider.credit_card_expiration_date()
    month, year = map(int, expiration_date.split('/'))
    assert 1 <= month <= 12
    assert 16 <= year <= 25

    # Test with custom parameters
    expiration_date = payment_provider.credit_card_expiration_date(minimum=20, maximum=30)
    month, year = map(int, expiration_date.split('/'))
    assert 1 <= month <= 12
    assert 20 <= year <= 30

    # Test edge cases
    expiration_date = payment_provider.credit_card_expiration_date(minimum=25, maximum=25)
    month, year = map(int, expiration_date.split('/'))
    assert 1 <= month <= 12
    assert year == 25

    expiration_date = payment_provider.credit_card_expiration_date(minimum=16, maximum=16)
    month, year = map(int, expiration_date.split('/'))
    assert 1 <= month <= 12
    assert year == 16
