# file mimesis/providers/payment.py:95-133
# lines [95, 105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 118, 119, 120, 121, 123, 125, 126, 127, 129, 130, 131, 132, 133]
# branches ['108->109', '108->111', '111->112', '111->113', '113->114', '113->118', '118->119', '118->123', '126->127', '126->129']

import pytest
from mimesis.enums import CardType
from mimesis.providers.payment import Payment
from mimesis.exceptions import NonEnumerableError

def test_credit_card_number_visa(mocker):
    payment = Payment()
    mocker.patch.object(payment.random, 'randint', return_value=4000)
    card_number = payment.credit_card_number(card_type=CardType.VISA)
    assert card_number.startswith('4000')
    assert len(card_number.replace(' ', '')) == 16

def test_credit_card_number_master_card(mocker):
    payment = Payment()
    mocker.patch.object(payment.random, 'choice', side_effect=lambda x: x[0])
    mocker.patch.object(payment.random, 'randint', return_value=2221)
    card_number = payment.credit_card_number(card_type=CardType.MASTER_CARD)
    assert card_number.startswith('2221')
    assert len(card_number.replace(' ', '')) == 16

def test_credit_card_number_american_express(mocker):
    payment = Payment()
    mocker.patch.object(payment.random, 'choice', side_effect=lambda x: 34 if x == [34, 37] else '0')
    card_number = payment.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
    assert card_number.startswith('34')
    assert len(card_number.replace(' ', '')) == 15

def test_credit_card_number_unsupported_card_type():
    payment = Payment()
    with pytest.raises(NonEnumerableError):
        payment.credit_card_number(card_type="UnsupportedCardType")
