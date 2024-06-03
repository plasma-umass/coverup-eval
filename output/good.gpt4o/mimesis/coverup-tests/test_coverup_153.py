# file mimesis/providers/payment.py:47-55
# lines [47, 55]
# branches []

import pytest
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person

@pytest.fixture
def mock_person(mocker):
    mock_person = mocker.patch('mimesis.providers.payment.Person')
    mock_person_instance = mock_person.return_value
    mock_person_instance.email.return_value = 'test@example.com'
    return mock_person_instance

def test_paypal(mock_person):
    payment = Payment()
    result = payment.paypal()
    assert result == 'test@example.com'
    mock_person.email.assert_called_once()
