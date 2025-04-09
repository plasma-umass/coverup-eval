# file pypara/monetary.py:313-320
# lines [319]
# branches ['318->319']

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, NoMoney, SomeMoney, Currency
from unittest.mock import patch

class MockCurrency(Currency):
    def __init__(self):
        super().__init__('USD', 'US Dollar', 2, 'fiat', Decimal('0.01'), None)

    def quantize(self, qty):
        return qty

def test_money_of_returns_nomoney_when_qty_is_none():
    result = Money.of(MockCurrency(), None, Date.today())
    assert result == NoMoney

def test_money_of_returns_nomoney_when_ccy_is_none():
    result = Money.of(None, Decimal('10.00'), Date.today())
    assert result == NoMoney

def test_money_of_returns_nomoney_when_dov_is_none():
    result = Money.of(MockCurrency(), Decimal('10.00'), None)
    assert result == NoMoney

def test_money_of_returns_somemoney():
    ccy = MockCurrency()
    qty = Decimal('10.00')
    dov = Date.today()
    with patch('pypara.monetary.SomeMoney') as MockSomeMoney:
        result = Money.of(ccy, qty, dov)
        MockSomeMoney.assert_called_once_with(ccy, qty, dov)
        assert result == MockSomeMoney.return_value
