# file: pypara/monetary.py:1164-1180
# asked: {"lines": [1164, 1165, 1166, 1174, 1175, 1177, 1178, 1180], "branches": [[1165, 1166], [1165, 1168], [1177, 1178], [1177, 1180]]}
# gained: {"lines": [1164, 1165, 1166, 1174, 1175, 1177, 1178, 1180], "branches": [[1165, 1166], [1165, 1168], [1177, 1178], [1177, 1180]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice, IncompatibleCurrencyError

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur_currency():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

class MockPrice(SomePrice):
    @property
    def undefined(self):
        return self._undefined

    @undefined.setter
    def undefined(self, value):
        self._undefined = value

def test_subtract_with_undefined_other(usd_currency):
    price1 = SomePrice(usd_currency, Decimal('100.0'), Date(2023, 1, 1))
    price2 = MockPrice(usd_currency, Decimal('0.0'), Date(2023, 1, 1))
    price2.undefined = True  # Mocking undefined attribute
    result = price1.subtract(price2)
    assert result == price1

def test_subtract_with_different_currencies(usd_currency, eur_currency):
    price1 = SomePrice(usd_currency, Decimal('100.0'), Date(2023, 1, 1))
    price2 = SomePrice(eur_currency, Decimal('50.0'), Date(2023, 1, 1))
    with pytest.raises(IncompatibleCurrencyError):
        price1.subtract(price2)

def test_subtract_with_same_currency(usd_currency):
    price1 = SomePrice(usd_currency, Decimal('100.0'), Date(2023, 1, 1))
    price2 = SomePrice(usd_currency, Decimal('50.0'), Date(2023, 1, 2))
    result = price1.subtract(price2)
    assert result.ccy == price1.ccy
    assert result.qty == Decimal('50.0')
    assert result.dov == price2.dov
