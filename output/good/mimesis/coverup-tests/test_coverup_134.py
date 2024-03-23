# file mimesis/providers/payment.py:95-133
# lines [95, 105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 118, 119, 120, 121, 123, 125, 126, 127, 129, 130, 131, 132, 133]
# branches ['108->109', '108->111', '111->112', '111->113', '113->114', '113->118', '118->119', '118->123', '126->127', '126->129']

import pytest
from mimesis.enums import CardType
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.payment import Payment
from mimesis.providers.base import BaseProvider
from unittest.mock import Mock

class TestPayment:

    @pytest.fixture
    def payment_provider(self):
        payment = Payment()
        payment.random = Mock()
        payment.random.randint.side_effect = lambda *args, **kwargs: args[0]
        payment.random.choice.side_effect = lambda *args, **kwargs: args[0][0]
        return payment

    def test_credit_card_number_visa(self, payment_provider):
        payment_provider.random.randint.return_value = 4000
        card_number = payment_provider.credit_card_number(card_type=CardType.VISA)
        assert card_number.startswith('4000')
        assert len(card_number.replace(' ', '')) == 16

    def test_credit_card_number_mastercard(self, payment_provider):
        payment_provider.random.choice.return_value = 2221
        payment_provider.random.randint.return_value = 2221
        card_number = payment_provider.credit_card_number(card_type=CardType.MASTER_CARD)
        assert card_number.startswith('2221')
        assert len(card_number.replace(' ', '')) == 16

    def test_credit_card_number_american_express(self, payment_provider):
        payment_provider.random.choice.return_value = 34
        card_number = payment_provider.credit_card_number(card_type=CardType.AMERICAN_EXPRESS)
        assert card_number.startswith('34')
        assert len(card_number.replace(' ', '')) == 15

    def test_credit_card_number_unsupported(self, payment_provider):
        with pytest.raises(NonEnumerableError):
            payment_provider.credit_card_number(card_type="Unsupported")

    def test_credit_card_number_random(self, payment_provider):
        card_number = payment_provider.credit_card_number()
        assert len(card_number.replace(' ', '')) in (15, 16)
