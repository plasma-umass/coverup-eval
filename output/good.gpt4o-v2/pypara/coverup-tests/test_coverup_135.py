# file: pypara/monetary.py:1046-1048
# asked: {"lines": [1046, 1047, 1048], "branches": []}
# gained: {"lines": [1046, 1047], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestPrice(Price):
    def __init__(self, ccy, qty, dov):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov

    def is_equal(self, other):
        return isinstance(other, TestPrice) and self.qty == other.qty

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return TestPrice(self.ccy, abs(self.qty), self.dov)

    def negative(self):
        return TestPrice(self.ccy, -self.qty, self.dov)

    def positive(self):
        return TestPrice(self.ccy, +self.qty, self.dov)

    def round(self, ndigits=0):
        return TestPrice(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other):
        return TestPrice(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other):
        return TestPrice(self.ccy, self.qty + other, self.dov)

    def subtract(self, other):
        return TestPrice(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other):
        return TestPrice(self.ccy, self.qty - other, self.dov)

    def multiply(self, other):
        return TestPrice(self.ccy, self.qty * other, self.dov)

    def times(self, other):
        return self.multiply(other)

    def divide(self, other):
        return TestPrice(self.ccy, self.qty / other, self.dov)

    def floor_divide(self, other):
        return TestPrice(self.ccy, self.qty // other, self.dov)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return TestPrice(ccy, self.qty, self.dov)

    def with_qty(self, qty):
        return TestPrice(self.ccy, qty, self.dov)

    def with_dov(self, dov):
        return TestPrice(self.ccy, self.qty, dov)

    def convert(self, to, asof=None, strict=False):
        return TestPrice(to, self.qty, self.dov)

    @property
    def money(self):
        return self.qty

    def __bool__(self):
        return bool(self.qty)

    def __eq__(self, other):
        return self.is_equal(other)

    def __abs__(self):
        return self.abs()

    def __float__(self):
        return self.as_float()

    def __int__(self):
        return self.as_integer()

    def __round__(self, ndigits=None):
        if ndigits is None:
            return round(self.qty)
        return TestPrice(self.ccy, round(self.qty, ndigits), self.dov)

    def __neg__(self):
        return self.negative()

    def __pos__(self):
        return self.positive()

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __floordiv__(self, other):
        return self.floor_divide(other)

    def __lt__(self, other):
        return self.lt(other)

    def __le__(self, other):
        return self.lte(other)

    def __gt__(self, other):
        return self.gt(other)

    def __ge__(self, other):
        return self.gte(other)

@pytest.fixture
def price():
    return TestPrice(Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), Decimal('100.00'), Date(2023, 1, 1))

def test_round_no_ndigits(price):
    result = round(price)
    assert result == 100

def test_round_with_ndigits_none(price):
    result = price.__round__(None)
    assert result == 100

def test_round_with_ndigits(price):
    result = round(price, 1)
    assert result.qty == Decimal('100.0')
