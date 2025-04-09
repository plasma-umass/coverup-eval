# file mimesis/providers/payment.py:160-172
# lines [160, 167, 168, 169, 170, 172]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.providers.payment import Payment

@pytest.fixture
def payment_provider(mocker):
    # Mock the full_name method of the Person provider used by Payment
    mocker.patch('mimesis.providers.person.Person.full_name', return_value="Mock Full Name")
    return Payment()

def test_credit_card_owner(payment_provider):
    # Test with no gender specified
    owner_no_gender = payment_provider.credit_card_owner()
    assert 'credit_card' in owner_no_gender
    assert 'expiration_date' in owner_no_gender
    assert owner_no_gender['owner'] == "MOCK FULL NAME"

    # Test with a specific gender
    owner_with_gender = payment_provider.credit_card_owner(gender=Gender.MALE)
    assert 'credit_card' in owner_with_gender
    assert 'expiration_date' in owner_with_gender
    assert owner_with_gender['owner'] == "MOCK FULL NAME"
