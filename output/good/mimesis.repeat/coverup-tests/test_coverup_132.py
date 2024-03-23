# file mimesis/providers/payment.py:47-55
# lines [47, 55]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person

# Mock the Person provider's email method
@pytest.fixture
def mock_person_provider(mocker):
    mock_person = mocker.patch.object(Person, 'email', return_value='mock_email@example.com')
    return mock_person

# Test the Payment provider's paypal method
def test_paypal(mock_person_provider):
    payment_provider = Payment()
    paypal_email = payment_provider.paypal()
    assert paypal_email == 'mock_email@example.com'
    mock_person_provider.assert_called_once()
