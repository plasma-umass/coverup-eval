# file mimesis/providers/payment.py:47-55
# lines [47, 55]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person
from unittest.mock import patch

# Test function to cover the paypal method in Payment class
def test_paypal(mocker):
    # Mock the Person class used within Payment class
    mocker.patch.object(Person, 'email', return_value='test@example.com')

    # Create an instance of Payment
    payment_provider = Payment()

    # Call the paypal method
    paypal_email = payment_provider.paypal()

    # Assert that the returned email is the one we mocked
    assert paypal_email == 'test@example.com'
