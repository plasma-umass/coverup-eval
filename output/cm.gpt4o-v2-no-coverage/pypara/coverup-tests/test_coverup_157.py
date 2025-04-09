# file: pypara/monetary.py:1129-1131
# asked: {"lines": [1129, 1130, 1131], "branches": []}
# gained: {"lines": [1129, 1130, 1131], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice, Price
from collections import namedtuple

MockPriceBase = namedtuple("MockPriceBase", ["ccy", "qty", "dov"])

class MockPrice(Price, MockPriceBase):
    def is_equal(self, other):
        return self == other

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
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return MockPrice(ccy, self.qty, self.dov)

    def with_qty(self, qty):
        return MockPrice(self.ccy, qty, self.dov)

    def with_dov(self, dov):
        return MockPrice(self.ccy, self.qty, dov)

    def convert(self, to, asof=None, strict=False):
        return MockPrice(to, self.qty, asof or self.dov)

    @property
    def money(self):
        return self.qty

    @classmethod
    def of(cls, ccy, qty, dov):
        return cls(ccy, qty, dov)

    def __bool__(self):
        return bool(self.qty)

    def __eq__(self, other):
        return self.ccy == other.ccy and self.qty == other.qty and self.dov == other.dov

    def __abs__(self):
        return abs(self.qty)

    def __float__(self):
        return float(self.qty)

    def __int__(self):
        return int(self.qty)

    def __round__(self, ndigits=0):
        return round(self.qty, ndigits)

    def __neg__(self):
        return -self.qty

    def __pos__(self):
        return +self.qty

    def __add__(self, other):
        return self.qty + other.qty

    def __sub__(self, other):
        return self.qty - other.qty

    def __mul__(self, other):
        return self.qty * other

    def __truediv__(self, other):
        return self.qty / other

    def __floordiv__(self, other):
        return self.qty // other

    def __lt__(self, other):
        return self.qty < other.qty

    def __le__(self, other):
        return self.qty <= other.qty

    def __gt__(self, other):
        return self.qty > other.qty

    def __ge__(self, other):
        return self.qty >= other.qty

@pytest.fixture
def mock_price():
    return MockPrice(Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), Decimal("100.00"), Date(2023, 1, 1))

def test_some_price_negative(mock_price):
    some_price = SomePrice(mock_price.ccy, mock_price.qty, mock_price.dov)
    neg_price = some_price.negative()
    assert neg_price.qty == -mock_price.qty
    assert neg_price.ccy == mock_price.ccy
    assert neg_price.dov == mock_price.dov
