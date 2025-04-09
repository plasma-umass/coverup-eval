# file: pypara/monetary.py:450-466
# asked: {"lines": [451, 452, 460, 461, 463, 464, 466], "branches": [[451, 452], [451, 454], [463, 464], [463, 466]]}
# gained: {"lines": [451, 452, 460, 461, 463, 464, 466], "branches": [[451, 452], [451, 454], [463, 464], [463, 466]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney, IncompatibleCurrencyError

USD = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
EUR = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

class MockMoney(SomeMoney):
    @property
    def undefined(self):
        return False

def test_add_same_currency():
    money1 = MockMoney(USD, Decimal("100.00"), Date(2023, 1, 1))
    money2 = MockMoney(USD, Decimal("50.00"), Date(2023, 1, 2))
    result = money1.add(money2)
    assert result.ccy == USD
    assert result.qty == Decimal("150.00")
    assert result.dov == Date(2023, 1, 2)

def test_add_different_currency():
    money1 = MockMoney(USD, Decimal("100.00"), Date(2023, 1, 1))
    money2 = MockMoney(EUR, Decimal("50.00"), Date(2023, 1, 2))
    with pytest.raises(IncompatibleCurrencyError):
        money1.add(money2)

def test_add_undefined_money(monkeypatch):
    money1 = MockMoney(USD, Decimal("100.00"), Date(2023, 1, 1))
    
    class UndefinedMoney(MockMoney):
        @property
        def undefined(self):
            return True
    
    money2 = UndefinedMoney(USD, Decimal("50.00"), Date(2023, 1, 2))
    result = money1.add(money2)
    assert result.ccy == money1.ccy
    assert result.qty == money1.qty
    assert result.dov == money1.dov
