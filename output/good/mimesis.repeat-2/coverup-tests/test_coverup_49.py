# file mimesis/providers/payment.py:135-148
# lines [135, 136, 146, 147, 148]
# branches []

import pytest
from mimesis.providers.payment import Payment

@pytest.fixture
def payment_provider():
    return Payment()

def test_credit_card_expiration_date(payment_provider):
    # Test the default range
    expiration_date = payment_provider.credit_card_expiration_date()
    month, year = expiration_date.split('/')
    assert int(month) in range(1, 13)
    assert int(year) in range(16, 26)

    # Test a custom range
    expiration_date_custom = payment_provider.credit_card_expiration_date(minimum=20, maximum=30)
    month_custom, year_custom = expiration_date_custom.split('/')
    assert int(month_custom) in range(1, 13)
    assert int(year_custom) in range(20, 31)

    # Test the edge cases
    expiration_date_edge = payment_provider.credit_card_expiration_date(minimum=25, maximum=25)
    month_edge, year_edge = expiration_date_edge.split('/')
    assert int(month_edge) in range(1, 13)
    assert int(year_edge) == 25
