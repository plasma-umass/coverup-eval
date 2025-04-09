# file: pypara/monetary.py:358-360
# asked: {"lines": [358, 359, 360], "branches": []}
# gained: {"lines": [358, 359], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, qty):
        self.qty = Decimal(qty)

    def is_equal(self, other):
        return self.qty == other.qty

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return ConcreteMoney(abs(self.qty))

    def negative(self):
        return ConcreteMoney(-self.qty)

    def positive(self):
        return ConcreteMoney(+self.qty)

    def round(self, ndigits=0):
        return ConcreteMoney(round(self.qty, ndigits))

    def add(self, other):
        return ConcreteMoney(self.qty + other.qty)

    def scalar_add(self, other):
        return ConcreteMoney(self.qty + other)

    def subtract(self, other):
        return ConcreteMoney(self.qty - other.qty)

    def scalar_subtract(self, other):
        return ConcreteMoney(self.qty - other)

    def multiply(self, other):
        return ConcreteMoney(self.qty * other)

    def divide(self, other):
        return ConcreteMoney(self.qty / other)

    def floor_divide(self, other):
        return ConcreteMoney(self.qty // other)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return self

    def with_qty(self, qty):
        return ConcreteMoney(qty)

    def with_dov(self, dov):
        return self

    def convert(self, to, asof=None, strict=False):
        return self

    @property
    def price(self):
        return self

    def __bool__(self):
        return bool(self.qty)

    def __eq__(self, other):
        return self.qty == other.qty

    def __abs__(self):
        return ConcreteMoney(abs(self.qty))

    def __float__(self):
        return float(self.qty)

    def __int__(self):
        return int(self.qty)

    def __round__(self, ndigits=0):
        if ndigits is None:
            return int(round(self.qty))
        return ConcreteMoney(round(self.qty, ndigits))

    def __neg__(self):
        return ConcreteMoney(-self.qty)

    def __pos__(self):
        return ConcreteMoney(+self.qty)

    def __add__(self, other):
        return ConcreteMoney(self.qty + other.qty)

    def __sub__(self, other):
        return ConcreteMoney(self.qty - other.qty)

    def __mul__(self, other):
        return ConcreteMoney(self.qty * other)

    def __truediv__(self, other):
        return ConcreteMoney(self.qty / other)

    def __floordiv__(self, other):
        return ConcreteMoney(self.qty // other)

    def __lt__(self, other):
        return self.qty < other.qty

    def __le__(self, other):
        return self.qty <= other.qty

    def __gt__(self, other):
        return self.qty > other.qty

    def __ge__(self, other):
        return self.qty >= other.qty

def test_money_round_with_ndigits():
    money = ConcreteMoney(123.456)
    rounded_money = round(money, 2)
    assert isinstance(rounded_money, Money)
    assert rounded_money.qty == Decimal('123.46')

def test_money_round_without_ndigits():
    money = ConcreteMoney(123.456)
    rounded_value = round(money)
    assert isinstance(rounded_value, Money)
    assert rounded_value.qty == Decimal('123')
