# file: pypara/monetary.py:653-654
# asked: {"lines": [653, 654], "branches": []}
# gained: {"lines": [653, 654], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney, Money
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class ConcreteMoney(Money):
    def __init__(self, qty, ccy):
        self.qty = Decimal(qty)
        self.ccy = ccy
        self.dov = Date.today()
        self.defined = True
        self.undefined = False

    def is_equal(self, other):
        return self.qty == other.qty and self.ccy == other.ccy

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return ConcreteMoney(abs(self.qty), self.ccy)

    def negative(self):
        return ConcreteMoney(-self.qty, self.ccy)

    def positive(self):
        return ConcreteMoney(+self.qty, self.ccy)

    def round(self, ndigits=0):
        return ConcreteMoney(round(self.qty, ndigits), self.ccy)

    def add(self, other):
        return ConcreteMoney(self.qty + other.qty, self.ccy)

    def scalar_add(self, other):
        return ConcreteMoney(self.qty + other, self.ccy)

    def subtract(self, other):
        return ConcreteMoney(self.qty - other.qty, self.ccy)

    def scalar_subtract(self, other):
        return ConcreteMoney(self.qty - other, self.ccy)

    def multiply(self, other):
        return ConcreteMoney(self.qty * other, self.ccy)

    def divide(self, other):
        return ConcreteMoney(self.qty / other, self.ccy)

    def floor_divide(self, other):
        return ConcreteMoney(self.qty // other, self.ccy)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return ConcreteMoney(self.qty, ccy)

    def with_qty(self, qty):
        return ConcreteMoney(qty, self.ccy)

    def with_dov(self, dov):
        return ConcreteMoney(self.qty, self.ccy)

    def convert(self, to, asof=None, strict=False):
        return ConcreteMoney(self.qty, to)

    @property
    def price(self):
        return self.qty

    def __bool__(self):
        return self.as_boolean()

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

def test_none_money_add():
    none_money = NoneMoney()
    other_money = ConcreteMoney(100, Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY))
    
    result = none_money.add(other_money)
    
    assert result == other_money
