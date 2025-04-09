# file: pypara/monetary.py:1233-1238
# asked: {"lines": [1233, 1234, 1235, 1236, 1237, 1238], "branches": [[1234, 1235], [1234, 1236], [1236, 1237], [1236, 1238]]}
# gained: {"lines": [1233, 1234, 1235, 1236, 1237, 1238], "branches": [[1234, 1235], [1234, 1236], [1236, 1237], [1236, 1238]]}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date

@pytest.fixture
def usd():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

class MockUndefinedPrice(SomePrice):
    @property
    def undefined(self):
        return True

def test_someprice_gte_with_undefined_other(usd):
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    price2 = MockUndefinedPrice(ccy=usd, qty=Decimal("5.00"), dov=Date(2023, 1, 1))
    assert price1.gte(price2) is True

def test_someprice_gte_with_different_currency(usd, eur):
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    price2 = SomePrice(ccy=eur, qty=Decimal("5.00"), dov=Date(2023, 1, 1))
    with pytest.raises(IncompatibleCurrencyError):
        price1.gte(price2)

def test_someprice_gte_with_greater_qty(usd):
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    price2 = SomePrice(ccy=usd, qty=Decimal("5.00"), dov=Date(2023, 1, 1))
    assert price1.gte(price2) is True

def test_someprice_gte_with_lesser_qty(usd):
    price1 = SomePrice(ccy=usd, qty=Decimal("5.00"), dov=Date(2023, 1, 1))
    price2 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    assert price1.gte(price2) is False

def test_someprice_gte_with_equal_qty(usd):
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    price2 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    assert price1.gte(price2) is True
