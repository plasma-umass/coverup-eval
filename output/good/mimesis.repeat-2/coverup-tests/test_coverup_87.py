# file mimesis/providers/payment.py:32-35
# lines [32, 33, 35]
# branches []

import pytest
from mimesis.providers.payment import Payment

def test_payment_meta():
    payment = Payment()
    assert payment.Meta.name == 'payment'
