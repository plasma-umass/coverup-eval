# file mimesis/providers/payment.py:95-133
# lines [123]
# branches ['108->111', '118->123']

import pytest
from mimesis.enums import CardType
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.payment import Payment
from unittest.mock import patch, MagicMock

class TestPayment:

    @pytest.fixture
    def payment_provider(self):
        with patch('mimesis.providers.payment.Payment.__init__', return_value=None):
            payment = Payment()
            payment.random = MagicMock()
            payment.random.randint.return_value = 4000
            payment.random.choice.return_value = '5'
            return payment

    def test_credit_card_number_with_unsupported_card_type(self, payment_provider):
        with pytest.raises(NonEnumerableError):
            payment_provider.credit_card_number(card_type="UnsupportedCardType")

    def test_credit_card_number_with_no_card_type(self, payment_provider):
        with patch('mimesis.providers.payment.get_random_item', return_value=CardType.VISA):
            card_number = payment_provider.credit_card_number()
            assert card_number.startswith('4') and len(card_number.replace(' ', '')) == 16
