# file: pypara/monetary.py:450-466
# asked: {"lines": [451, 452, 460, 461, 463, 464, 466], "branches": [[451, 452], [451, 454], [463, 464], [463, 466]]}
# gained: {"lines": [451, 452, 460, 461, 463, 464, 466], "branches": [[451, 452], [451, 454], [463, 464], [463, 466]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney, IncompatibleCurrencyError

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur_currency():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

def test_add_undefined_money(usd_currency):
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    money1 = SomeMoney(usd_currency, qty, dov)
    
    class UndefinedMoney:
        undefined = True
    
    money2 = UndefinedMoney()
    
    result = money1.add(money2)
    assert result == money1

def test_add_incompatible_currency(usd_currency, eur_currency):
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    money1 = SomeMoney(usd_currency, qty, dov)
    money2 = SomeMoney(eur_currency, qty, dov)
    
    with pytest.raises(IncompatibleCurrencyError) as excinfo:
        money1.add(money2)
    
    assert excinfo.value.ccy1 == usd_currency
    assert excinfo.value.ccy2 == eur_currency
    assert excinfo.value.operation == "addition"

def test_add_compatible_currency(usd_currency):
    qty1 = Decimal("100.00")
    qty2 = Decimal("50.00")
    dov1 = Date(2023, 10, 1)
    dov2 = Date(2023, 9, 1)
    money1 = SomeMoney(usd_currency, qty1, dov1)
    money2 = SomeMoney(usd_currency, qty2, dov2)
    
    result = money1.add(money2)
    assert result.ccy == usd_currency
    assert result.qty == qty1 + qty2
    assert result.dov == dov1
