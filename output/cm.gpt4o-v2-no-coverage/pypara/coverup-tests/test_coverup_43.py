# file: pypara/monetary.py:501-507
# asked: {"lines": [501, 503, 504, 505, 506, 507], "branches": []}
# gained: {"lines": [501, 503, 504, 505, 506, 507], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from datetime import date as Date
from pypara.monetary import SomeMoney, Money, NoMoney
from pypara.currencies import Currency

class MockCurrency:
    def __init__(self, quantizer):
        self.quantizer = quantizer

class MockMoney(Money):
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
        return MockMoney(self.ccy, abs(self.qty), self.dov)

    def negative(self):
        return MockMoney(self.ccy, -self.qty, self.dov)

    def positive(self):
        return MockMoney(self.ccy, +self.qty, self.dov)

    def round(self, ndigits=0):
        return MockMoney(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other):
        return MockMoney(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other):
        return MockMoney(self.ccy, self.qty + Decimal(other), self.dov)

    def subtract(self, other):
        return MockMoney(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other):
        return MockMoney(self.ccy, self.qty - Decimal(other), self.dov)

    def multiply(self, other):
        return MockMoney(self.ccy, self.qty * Decimal(other), self.dov)

    def divide(self, other):
        return MockMoney(self.ccy, self.qty / Decimal(other), self.dov)

    def floor_divide(self, other):
        return MockMoney(self.ccy, self.qty // Decimal(other), self.dov)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return MockMoney(ccy, self.qty, self.dov)

    def with_qty(self, qty):
        return MockMoney(self.ccy, qty, self.dov)

    def with_dov(self, dov):
        return MockMoney(self.ccy, self.qty, dov)

    def convert(self, to, asof=None, strict=False):
        return MockMoney(to, self.qty, asof or self.dov)

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
def mock_currency():
    return MockCurrency(Decimal('0.01'))

@pytest.fixture
def some_money(mock_currency):
    return SomeMoney(mock_currency, Decimal('100.00'), Date(2023, 1, 1))

def test_divide_by_valid_number(some_money):
    result = some_money.divide(2)
    assert result.qty == Decimal('50.00')

def test_divide_by_zero(some_money):
    result = some_money.divide(0)
    assert result == NoMoney

def test_divide_by_invalid_operation(some_money):
    result = some_money.divide('invalid')
    assert result == NoMoney
