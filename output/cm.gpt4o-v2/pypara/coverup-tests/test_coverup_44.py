# file: pypara/monetary.py:501-507
# asked: {"lines": [501, 503, 504, 505, 506, 507], "branches": []}
# gained: {"lines": [501, 503, 504, 505, 506, 507], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomeMoney, NoMoney
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date

def test_divide_valid():
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    money = SomeMoney(currency, Decimal("100.00"), Date.today())
    result = money.divide(2)
    assert result.qty == Decimal("50.00")
    assert result.ccy == currency
    assert result.dov == money.dov

def test_divide_invalid_operation():
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    money = SomeMoney(currency, Decimal("100.00"), Date.today())
    result = money.divide("invalid")
    assert result == NoMoney

def test_divide_division_by_zero():
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    money = SomeMoney(currency, Decimal("100.00"), Date.today())
    result = money.divide(0)
    assert result == NoMoney
