# file: pypara/monetary.py:473-489
# asked: {"lines": [473, 474, 475, 483, 484, 486, 487, 489], "branches": [[474, 475], [474, 477], [486, 487], [486, 489]]}
# gained: {"lines": [473, 474, 475, 483, 484, 486, 487, 489], "branches": [[474, 475], [474, 477], [486, 487], [486, 489]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney, IncompatibleCurrencyError, Money

@pytest.fixture
def usd():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

@pytest.fixture
def undefined_money():
    return Money.NA

def test_subtract_same_currency(usd):
    qty1 = Decimal("100.00")
    qty2 = Decimal("50.00")
    dov1 = Date(2023, 1, 1)
    dov2 = Date(2023, 1, 2)
    
    money1 = SomeMoney(usd, qty1, dov1)
    money2 = SomeMoney(usd, qty2, dov2)
    
    result = money1.subtract(money2)
    
    assert result.ccy == usd
    assert result.qty == Decimal("50.00")
    assert result.dov == dov2

def test_subtract_different_currency(usd, eur):
    qty1 = Decimal("100.00")
    qty2 = Decimal("50.00")
    dov1 = Date(2023, 1, 1)
    dov2 = Date(2023, 1, 2)
    
    money1 = SomeMoney(usd, qty1, dov1)
    money2 = SomeMoney(eur, qty2, dov2)
    
    with pytest.raises(IncompatibleCurrencyError):
        money1.subtract(money2)

def test_subtract_undefined_other(usd, undefined_money):
    qty1 = Decimal("100.00")
    qty2 = Decimal("50.00")
    dov1 = Date(2023, 1, 1)
    dov2 = Date(2023, 1, 2)
    
    money1 = SomeMoney(usd, qty1, dov1)
    money2 = undefined_money
    
    result = money1.subtract(money2)
    
    assert result == money1
