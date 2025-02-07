# file: pypara/monetary.py:1212-1217
# asked: {"lines": [1213, 1214, 1215, 1216, 1217], "branches": [[1213, 1214], [1213, 1215], [1215, 1216], [1215, 1217]]}
# gained: {"lines": [1213, 1214, 1215, 1216, 1217], "branches": [[1213, 1214], [1213, 1215], [1215, 1216], [1215, 1217]]}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, IncompatibleCurrencyError, Price
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur_currency():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

class MockPrice(Price):
    def __init__(self, ccy, qty, dov, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.undefined = undefined

    def is_equal(self, other):
        return self.ccy == other.ccy and self.qty == other.qty and self.dov == other.dov

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return MockPrice(self.ccy, abs(self.qty), self.dov)

    def negative(self):
        return MockPrice(self.ccy, -self.qty, self.dov)

    def positive(self):
        return MockPrice(self.ccy, +self.qty, self.dov)

    def round(self, ndigits=0):
        return MockPrice(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other):
        return MockPrice(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other):
        return MockPrice(self.ccy, self.qty + other, self.dov)

    def subtract(self, other):
        return MockPrice(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other):
        return MockPrice(self.ccy, self.qty - other, self.dov)

    def multiply(self, other):
        return MockPrice(self.ccy, self.qty * other, self.dov)

    def times(self, other):
        return MockPrice(self.ccy, self.qty * other, self.dov)

    def divide(self, other):
        return MockPrice(self.ccy, self.qty / other, self.dov)

    def floor_divide(self, other):
        return MockPrice(self.ccy, self.qty // other, self.dov)

    def lt(self, other):
        if other.undefined:
            return False
        elif self.ccy != other.ccy:
            raise IncompatibleCurrencyError(ccy1=self.ccy, ccy2=other.ccy, operation="< comparision")
        return self.qty < other.qty

    def lte(self, other):
        return self.lt(other) or self.is_equal(other)

    def gt(self, other):
        return not self.lte(other)

    def gte(self, other):
        return not self.lt(other)

    def with_ccy(self, ccy):
        return MockPrice(ccy, self.qty, self.dov)

    def with_qty(self, qty):
        return MockPrice(self.ccy, qty, self.dov)

    def with_dov(self, dov):
        return MockPrice(self.ccy, self.qty, dov)

    def convert(self, to, asof=None, strict=False):
        return MockPrice(to, self.qty, self.dov)

    @property
    def money(self):
        return self.qty

def test_someprice_lt_with_undefined_other(usd_currency):
    price1 = SomePrice(ccy=usd_currency, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    price2 = MockPrice(ccy=usd_currency, qty=Decimal("20.00"), dov=Date(2023, 1, 1), undefined=True)
    assert not price1.lt(price2)

def test_someprice_lt_with_incompatible_currency(usd_currency, eur_currency):
    price1 = SomePrice(ccy=usd_currency, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    price2 = SomePrice(ccy=eur_currency, qty=Decimal("20.00"), dov=Date(2023, 1, 1))
    with pytest.raises(IncompatibleCurrencyError) as excinfo:
        price1.lt(price2)
    assert str(excinfo.value) == "USD vs EUR are incompatible for operation '< comparision'."

def test_someprice_lt_with_compatible_currency(usd_currency):
    price1 = SomePrice(ccy=usd_currency, qty=Decimal("10.00"), dov=Date(2023, 1, 1))
    price2 = SomePrice(ccy=usd_currency, qty=Decimal("20.00"), dov=Date(2023, 1, 1))
    assert price1.lt(price2)
