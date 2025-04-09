# file: pypara/monetary.py:1141-1157
# asked: {"lines": [1141, 1142, 1143, 1151, 1152, 1154, 1155, 1157], "branches": [[1142, 1143], [1142, 1145], [1154, 1155], [1154, 1157]]}
# gained: {"lines": [1141, 1142, 1143, 1151, 1152, 1154, 1155, 1157], "branches": [[1142, 1143], [1142, 1145], [1154, 1155], [1154, 1157]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice, IncompatibleCurrencyError

class MockPrice:
    def __init__(self, ccy, qty, dov, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.undefined = undefined

    def __iter__(self):
        return iter((self.ccy, self.qty, self.dov))

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur_currency():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

@pytest.fixture
def some_price_usd(usd_currency):
    return SomePrice(usd_currency, Decimal("100.00"), Date(2023, 1, 1))

@pytest.fixture
def some_price_usd_undefined(usd_currency):
    return MockPrice(usd_currency, Decimal("100.00"), Date(2023, 1, 1), undefined=True)

@pytest.fixture
def some_price_eur(eur_currency):
    return SomePrice(eur_currency, Decimal("100.00"), Date(2023, 1, 1))

def test_add_undefined(some_price_usd, some_price_usd_undefined):
    result = some_price_usd.add(some_price_usd_undefined)
    assert result == some_price_usd

def test_add_incompatible_currency(some_price_usd, some_price_eur):
    with pytest.raises(IncompatibleCurrencyError):
        some_price_usd.add(some_price_eur)

def test_add_same_currency(some_price_usd):
    other_price = SomePrice(some_price_usd.ccy, Decimal("50.00"), Date(2023, 1, 2))
    result = some_price_usd.add(other_price)
    assert result.ccy == some_price_usd.ccy
    assert result.qty == Decimal("150.00")
    assert result.dov == Date(2023, 1, 2)
