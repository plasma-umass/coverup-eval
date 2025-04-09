# file: pypara/monetary.py:155-166
# asked: {"lines": [155, 156, 166], "branches": []}
# gained: {"lines": [155, 156], "branches": []}

import pytest
from abc import ABC
from pypara.monetary import Money, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from decimal import Decimal

class TestMoney(Money, ABC):
    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise IncompatibleCurrencyError(self.currency, other.currency)
        if self.amount is None:
            return other
        if other.amount is None:
            return self
        return TestMoney(self.amount + other.amount, self.currency)

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

def test_add_incompatible_currency():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    eur = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    money1 = TestMoney(100, usd)
    money2 = TestMoney(100, eur)
    with pytest.raises(IncompatibleCurrencyError):
        money1.add(money2)

def test_add_undefined_self():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money1 = TestMoney(None, usd)
    money2 = TestMoney(100, usd)
    result = money1.add(money2)
    assert result.amount == 100
    assert result.currency == usd

def test_add_undefined_other():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money1 = TestMoney(100, usd)
    money2 = TestMoney(None, usd)
    result = money1.add(money2)
    assert result.amount == 100
    assert result.currency == usd

def test_add_defined():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money1 = TestMoney(100, usd)
    money2 = TestMoney(50, usd)
    result = money1.add(money2)
    assert result.amount == 150
    assert result.currency == usd
