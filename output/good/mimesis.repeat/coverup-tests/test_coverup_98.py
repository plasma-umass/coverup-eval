# file mimesis/providers/payment.py:160-172
# lines [160, 167, 168, 169, 170, 172]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.providers.payment import Payment
from mimesis import Person
from unittest.mock import patch, MagicMock

@pytest.fixture
def payment_provider():
    return Payment()

@pytest.fixture
def person_provider():
    person = Person()
    person.full_name = MagicMock(side_effect=lambda gender=None: 'John Doe' if gender is None else ('Jane Doe' if gender == Gender.FEMALE else 'John Doe'))
    return person

def test_credit_card_owner_with_gender(payment_provider, person_provider):
    with patch.object(payment_provider, '_Payment__person', person_provider):
        for gender in Gender:
            owner = payment_provider.credit_card_owner(gender=gender)
            expected_name = 'Jane Doe' if gender == Gender.FEMALE else 'John Doe'
            assert owner['owner'] == expected_name.upper()
            assert 'credit_card' in owner
            assert 'expiration_date' in owner

def test_credit_card_owner_without_gender(payment_provider, person_provider):
    with patch.object(payment_provider, '_Payment__person', person_provider):
        owner = payment_provider.credit_card_owner()
        assert owner['owner'] == 'John Doe'.upper()
        assert 'credit_card' in owner
        assert 'expiration_date' in owner
