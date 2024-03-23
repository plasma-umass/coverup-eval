# file mimesis/providers/payment.py:23-30
# lines [23, 29, 30]
# branches []

import pytest
from mimesis.providers.payment import Payment

def test_payment_initialization(mocker):
    # Mock the Person class to ensure it is being called correctly
    mock_person = mocker.patch('mimesis.providers.payment.Person', autospec=True)

    # Create an instance of Payment with specific seed
    seed = 42
    payment = Payment(seed=seed)

    # Assert that the Person class was instantiated with the correct locale and seed
    mock_person.assert_called_once_with('en', seed=seed)

    # Clean up by deleting the payment instance
    del payment
