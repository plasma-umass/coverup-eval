# file mimesis/providers/payment.py:160-172
# lines [160, 167, 168, 169, 170, 172]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.providers import Person
from mimesis.providers.payment import Payment

# Mock the Person provider to control the output of full_name
@pytest.fixture
def mocked_person(mocker):
    person = mocker.patch('mimesis.providers.payment.Person', autospec=True)
    person_instance = person.return_value
    person_instance.full_name.return_value = 'John Doe'
    return person_instance

# Test function to cover credit_card_owner with a specific gender
def test_credit_card_owner_with_gender(mocked_person):
    payment = Payment()
    owner = payment.credit_card_owner(gender=Gender.MALE)
    assert owner['owner'] == 'JOHN DOE'
    mocked_person.full_name.assert_called_once_with(gender=Gender.MALE)

# Test function to cover credit_card_owner without specifying gender
def test_credit_card_owner_without_gender(mocked_person):
    payment = Payment()
    owner = payment.credit_card_owner()
    assert owner['owner'] == 'JOHN DOE'
    mocked_person.full_name.assert_called_once_with(gender=None)
