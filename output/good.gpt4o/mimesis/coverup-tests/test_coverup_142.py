# file mimesis/providers/payment.py:37-45
# lines [37, 45]
# branches []

import pytest
from mimesis.providers.payment import Payment

def test_cid(mocker):
    payment = Payment()
    
    # Mock the randint method to control the output
    mocker.patch.object(payment.random, 'randint', return_value=7452)
    
    cid = payment.cid()
    
    # Assert that the cid method returns the mocked value
    assert cid == 7452
