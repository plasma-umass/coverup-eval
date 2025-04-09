# file mimesis/providers/payment.py:23-30
# lines [23, 29, 30]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person

def test_payment_initialization(mocker):
    # Mock the Person class to ensure it is called with the correct parameters
    mock_person = mocker.patch('mimesis.providers.payment.Person', autospec=True)
    
    # Create an instance of Payment
    payment = Payment(seed=1234)
    
    # Assert that the Person class was instantiated with the correct parameters
    mock_person.assert_called_once_with('en', seed=1234)
    
    # Assert that the __person attribute is the mocked Person instance
    assert payment._Payment__person is mock_person.return_value
