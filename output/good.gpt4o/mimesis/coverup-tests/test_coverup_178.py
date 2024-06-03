# file mimesis/providers/payment.py:95-133
# lines [105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 118, 119, 120, 121, 123, 125, 126, 127, 129, 130, 131, 132, 133]
# branches ['108->109', '108->111', '111->112', '111->113', '113->114', '113->118', '118->119', '118->123', '126->127', '126->129']

import pytest
from mimesis.providers.payment import Payment, CardType
from mimesis.exceptions import NonEnumerableError

@pytest.fixture
def payment():
    return Payment()

def test_credit_card_number_visa(payment):
    card_number = payment.credit_card_number(CardType.VISA)
    assert len(card_number) == 19  # 16 digits + 3 spaces
    assert card_number.startswith('4')

def test_credit_card_number_master_card(payment):
    card_number = payment.credit_card_number(CardType.MASTER_CARD)
    assert len(card_number) == 19  # 16 digits + 3 spaces
    assert card_number.startswith(('2221', '2222', '2223', '2224', '2225', '2226', '2227', '2228', '2229', '223', '224', '225', '226', '227', '228', '229', '23', '24', '25', '26', '270', '271', '2720', '51', '52', '53', '54', '55'))

def test_credit_card_number_american_express(payment):
    card_number = payment.credit_card_number(CardType.AMERICAN_EXPRESS)
    assert len(card_number) == 17  # 15 digits + 2 spaces
    assert card_number.startswith(('34', '37'))

def test_credit_card_number_invalid_card_type(payment):
    with pytest.raises(NonEnumerableError):
        payment.credit_card_number("INVALID_CARD_TYPE")
