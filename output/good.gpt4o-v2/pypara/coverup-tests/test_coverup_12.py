# file: pypara/monetary.py:473-489
# asked: {"lines": [473, 474, 475, 483, 484, 486, 487, 489], "branches": [[474, 475], [474, 477], [486, 487], [486, 489]]}
# gained: {"lines": [473, 474, 475, 483, 484, 486, 487, 489], "branches": [[474, 475], [474, 477], [486, 487], [486, 489]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney, IncompatibleCurrencyError

@pytest.fixture
def usd():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

def test_subtract_undefined_other(usd):
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    money = SomeMoney(usd, qty, dov)
    
    class UndefinedMoney:
        undefined = True
    
    other = UndefinedMoney()
    
    result = money.subtract(other)
    assert result == money

def test_subtract_incompatible_currency(usd, eur):
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    money1 = SomeMoney(usd, qty, dov)
    money2 = SomeMoney(eur, qty, dov)
    
    with pytest.raises(IncompatibleCurrencyError) as excinfo:
        money1.subtract(money2)
    
    assert excinfo.value.ccy1 == usd
    assert excinfo.value.ccy2 == eur
    assert excinfo.value.operation == "subtraction"

def test_subtract_compatible_currency(usd):
    qty1 = Decimal("100.00")
    qty2 = Decimal("50.00")
    dov1 = Date(2023, 1, 1)
    dov2 = Date(2023, 1, 2)
    money1 = SomeMoney(usd, qty1, dov1)
    money2 = SomeMoney(usd, qty2, dov2)
    
    result = money1.subtract(money2)
    assert result.ccy == usd
    assert result.qty == qty1 - qty2
    assert result.dov == dov2
