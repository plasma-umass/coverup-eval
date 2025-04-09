# file: pypara/monetary.py:393-395
# asked: {"lines": [393, 394, 395], "branches": []}
# gained: {"lines": [393, 394], "branches": []}

import pytest
from decimal import Decimal
from unittest.mock import MagicMock
from pypara.monetary import Money
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class ConcreteMoney(Money):
    def __init__(self, ccy, qty, dov):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov

    def is_equal(self, other):
        return self.ccy == other.ccy and self.qty == other.qty and self.dov == other.dov

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return ConcreteMoney(self.ccy, abs(self.qty), self.dov)

    def negative(self):
        return ConcreteMoney(self.ccy, -self.qty, self.dov)

    def positive(self):
        return ConcreteMoney(self.ccy, +self.qty, self.dov)

    def round(self, ndigits=0):
        return ConcreteMoney(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other):
        return ConcreteMoney(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other):
        return ConcreteMoney(self.ccy, self.qty + other, self.dov)

    def subtract(self, other):
        return ConcreteMoney(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other):
        return ConcreteMoney(self.ccy, self.qty - other, self.dov)

    def multiply(self, other):
        return ConcreteMoney(self.ccy, self.qty * other, self.dov)

    def divide(self, other):
        return ConcreteMoney(self.ccy, self.qty / other, self.dov)

    def floor_divide(self, other):
        return ConcreteMoney(self.ccy, self.qty // other, self.dov)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return ConcreteMoney(ccy, self.qty, self.dov)

    def with_qty(self, qty):
        return ConcreteMoney(self.ccy, qty, self.dov)

    def with_dov(self, dov):
        return ConcreteMoney(self.ccy, self.qty, dov)

    def convert(self, to, asof=None, strict=False):
        return ConcreteMoney(to, self.qty, self.dov)

    @property
    def price(self):
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

    def __round__(self, ndigits=0):
        return self.round(ndigits)

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
def currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def money(currency):
    return ConcreteMoney(currency, Decimal("100.00"), Date(2023, 1, 1))

@pytest.fixture
def other_money(currency):
    return ConcreteMoney(currency, Decimal("50.00"), Date(2023, 1, 1))

def test_lt(money, other_money):
    assert not money < other_money
    assert other_money < money

def test_le(money, other_money):
    assert not money <= other_money
    assert other_money <= money
    assert money <= money

def test_gt(money, other_money):
    assert money > other_money
    assert not other_money > money

def test_ge(money, other_money):
    assert money >= other_money
    assert not other_money >= money
    assert money >= money
