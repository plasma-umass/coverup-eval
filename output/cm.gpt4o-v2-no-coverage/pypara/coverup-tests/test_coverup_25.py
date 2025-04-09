# file: pypara/monetary.py:509-515
# asked: {"lines": [509, 511, 512, 513, 514, 515], "branches": []}
# gained: {"lines": [509, 511, 512, 513, 514, 515], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomeMoney, NoMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_floor_divide_valid():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    money = SomeMoney(ccy, qty, dov)
    result = money.floor_divide(2)
    assert result.qty == Decimal("50.00")
    assert result.ccy == ccy
    assert result.dov == dov

def test_floor_divide_zero():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    money = SomeMoney(ccy, qty, dov)
    result = money.floor_divide(0)
    assert result == NoMoney

def test_floor_divide_invalid():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    money = SomeMoney(ccy, qty, dov)
    result = money.floor_divide("invalid")
    assert result == NoMoney
