# file: pypara/monetary.py:358-360
# asked: {"lines": [358, 359, 360], "branches": []}
# gained: {"lines": [358, 359], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Money
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestMoney(Money):
    def __init__(self, ccy, qty, dov):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov

    def is_equal(self, other):
        return self.qty == other.qty and self.ccy == other.ccy

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return TestMoney(self.ccy, abs(self.qty), self.dov)

    def negative(self):
        return TestMoney(self.ccy, -abs(self.qty), self.dov)

    def positive(self):
        return TestMoney(self.ccy, abs(self.qty), self.dov)

    def round(self, ndigits=0):
        return TestMoney(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other):
        return TestMoney(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other):
        return TestMoney(self.ccy, self.qty + other, self.dov)

    def subtract(self, other):
        return TestMoney(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other):
        return TestMoney(self.ccy, self.qty - other, self.dov)

    def multiply(self, other):
        return TestMoney(self.ccy, self.qty * other, self.dov)

    def divide(self, other):
        return TestMoney(self.ccy, self.qty / other, self.dov)

    def floor_divide(self, other):
        return TestMoney(self.ccy, self.qty // other, self.dov)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return TestMoney(ccy, self.qty, self.dov)

    def with_qty(self, qty):
        return TestMoney(self.ccy, qty, self.dov)

    def with_dov(self, dov):
        return TestMoney(self.ccy, self.qty, dov)

    def convert(self, to, asof=None, strict=False):
        return TestMoney(to, self.qty, self.dov)

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

    def __round__(self, ndigits=None):
        if ndigits is None:
            return int(self.qty)
        return self.round(ndigits)

@pytest.fixture
def money():
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    return TestMoney(currency, Decimal('100.00'), Date(2023, 1, 1))

def test_round_no_args(money):
    result = round(money)
    assert isinstance(result, int)

def test_round_with_none(money):
    result = round(money, None)
    assert isinstance(result, int)

def test_round_with_ndigits(money):
    result = round(money, 2)
    assert isinstance(result, TestMoney)
    assert result.qty == round(money.qty, 2)
