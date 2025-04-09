# file: pypara/monetary.py:1069-1071
# asked: {"lines": [1069, 1070, 1071], "branches": []}
# gained: {"lines": [1069, 1070], "branches": []}

import pytest
from decimal import Decimal
from unittest.mock import Mock
from pypara.monetary import Price
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class ConcretePrice(Price):
    def __init__(self, ccy, qty, dov):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov

    def __sub__(self, other):
        return ConcretePrice(self.ccy, self.qty - other.qty, self.dov)

    def is_equal(self, other):
        return self.qty == other.qty

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return ConcretePrice(self.ccy, abs(self.qty), self.dov)

    def negative(self):
        return ConcretePrice(self.ccy, -self.qty, self.dov)

    def positive(self):
        return ConcretePrice(self.ccy, +self.qty, self.dov)

    def round(self, ndigits=0):
        return ConcretePrice(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other):
        return ConcretePrice(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other):
        return ConcretePrice(self.ccy, self.qty + other, self.dov)

    def subtract(self, other):
        return ConcretePrice(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other):
        return ConcretePrice(self.ccy, self.qty - other, self.dov)

    def multiply(self, other):
        return ConcretePrice(self.ccy, self.qty * other, self.dov)

    def times(self, other):
        return ConcretePrice(self.ccy, self.qty * other, self.dov)

    def divide(self, other):
        return ConcretePrice(self.ccy, self.qty / other, self.dov)

    def floor_divide(self, other):
        return ConcretePrice(self.ccy, self.qty // other, self.dov)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return ConcretePrice(ccy, self.qty, self.dov)

    def with_qty(self, qty):
        return ConcretePrice(self.ccy, qty, self.dov)

    def with_dov(self, dov):
        return ConcretePrice(self.ccy, self.qty, dov)

    def convert(self, to, asof=None, strict=False):
        return ConcretePrice(to, self.qty, self.dov)

    @property
    def money(self):
        return self.qty

    @classmethod
    def of(cls, ccy, qty, dov):
        return cls(ccy, qty, dov)

    def __bool__(self):
        return bool(self.qty)

    def __eq__(self, other):
        return self.qty == other.qty

    def __abs__(self):
        return ConcretePrice(self.ccy, abs(self.qty), self.dov)

    def __float__(self):
        return float(self.qty)

    def __int__(self):
        return int(self.qty)

    def __round__(self, ndigits=0):
        return ConcretePrice(self.ccy, round(self.qty, ndigits), self.dov)

    def __neg__(self):
        return ConcretePrice(self.ccy, -self.qty, self.dov)

    def __pos__(self):
        return ConcretePrice(self.ccy, +self.qty, self.dov)

    def __add__(self, other):
        return ConcretePrice(self.ccy, self.qty + other.qty, self.dov)

    def __mul__(self, other):
        return ConcretePrice(self.ccy, self.qty * other, self.dov)

    def __truediv__(self, other):
        return ConcretePrice(self.ccy, self.qty / other, self.dov)

    def __floordiv__(self, other):
        return ConcretePrice(self.ccy, self.qty // other, self.dov)

    def __lt__(self, other):
        return self.qty < other.qty

    def __le__(self, other):
        return self.qty <= other.qty

    def __gt__(self, other):
        return self.qty > other.qty

    def __ge__(self, other):
        return self.qty >= other.qty

@pytest.fixture
def price():
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    return ConcretePrice(currency, Decimal('100.0'), Date(2023, 1, 1))

@pytest.fixture
def other_price():
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    return ConcretePrice(currency, Decimal('50.0'), Date(2023, 1, 1))

def test_sub(price, other_price):
    result = price - other_price
    assert result.qty == Decimal('50.0')
    assert result.ccy == price.ccy
    assert result.dov == price.dov
