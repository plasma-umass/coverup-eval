# file pypara/monetary.py:445-448
# lines [446, 447, 448]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, Currency, SomeMoney

class TestSomeMoney:
    def test_round_method(self):
        # Mocking Currency class
        class MockCurrency(Currency):
            def __init__(self, code):
                super().__init__(code, 'Mock Currency', 2, 'type', 'quantizer', 'hashcache')

        # Creating an instance of SomeMoney
        currency = MockCurrency('USD')
        quantity = Decimal('123.456')
        dov = Date(2023, 1, 1)
        some_money = SomeMoney(currency, quantity, dov)

        # Testing the round method
        rounded_money = some_money.round(1)
        assert rounded_money.qty == Decimal('123.5')
        assert rounded_money.ccy == currency
        assert rounded_money.dov == dov

        rounded_money = some_money.round(3)
        assert rounded_money.qty == Decimal('123.46')
        assert rounded_money.ccy == currency
        assert rounded_money.dov == dov
