# file mimesis/providers/payment.py:160-172
# lines [167, 168, 169, 170, 172]
# branches []

import pytest
from mimesis import Person
from mimesis.enums import Gender
from mimesis.providers.payment import Payment

@pytest.fixture
def payment_provider(mocker):
    mocker.patch('mimesis.providers.payment.Person', autospec=True)
    return Payment()

def test_credit_card_owner(payment_provider, mocker):
    mock_person = mocker.Mock(spec=Person)
    mock_person.full_name.return_value = 'John Doe'
    payment_provider._Payment__person = mock_person

    owner = payment_provider.credit_card_owner(gender=Gender.MALE)

    assert 'credit_card' in owner
    assert 'expiration_date' in owner
    assert 'owner' in owner
    assert owner['owner'] == 'JOHN DOE'
