# file: pypara/monetary.py:771-781
# asked: {"lines": [771, 772, 781], "branches": []}
# gained: {"lines": [771, 772], "branches": []}

import pytest
from decimal import Decimal
from unittest.mock import Mock
from pypara.monetary import Price
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestPrice(Price):
    def __init__(self, ccy, qty, dov):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov

    def is_equal(self, other):
        if not isinstance(other, Price):
            return False
        return self.ccy == other.ccy and self.qty == other.qty and self.dov == other.dov

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
def price():
    return TestPrice(Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY), Decimal('100.0'), Date(2023, 1, 1))

@pytest.fixture
def other_price():
    return TestPrice(Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY), Decimal('100.0'), Date(2023, 1, 1))

@pytest.fixture
def different_price():
    return TestPrice(Currency.of('EUR', 'Euro', 2, CurrencyType.MONEY), Decimal('200.0'), Date(2023, 1, 1))

def test_is_equal(price, other_price, different_price):
    assert price.is_equal(other_price)
    assert not price.is_equal(different_price)
    assert not price.is_equal("not a price")

def test_as_boolean(price):
    assert price.as_boolean() is True

def test_as_float(price):
    assert price.as_float() == 100.0

def test_as_integer(price):
    assert price.as_integer() == 100

def test_abs(price):
    negative_price = price.negative()
    assert negative_price.abs() == price

def test_negative(price):
    negative_price = price.negative()
    assert negative_price.qty == -price.qty

def test_positive(price):
    positive_price = price.positive()
    assert positive_price.qty == price.qty

def test_round(price):
    rounded_price = price.round()
    assert rounded_price.qty == round(price.qty)

def test_add(price, other_price):
    added_price = price.add(other_price)
    assert added_price.qty == price.qty + other_price.qty

def test_scalar_add(price):
    added_price = price.scalar_add(Decimal('50.0'))
    assert added_price.qty == price.qty + Decimal('50.0')

def test_subtract(price, other_price):
    subtracted_price = price.subtract(other_price)
    assert subtracted_price.qty == price.qty - other_price.qty

def test_scalar_subtract(price):
    subtracted_price = price.scalar_subtract(Decimal('50.0'))
    assert subtracted_price.qty == price.qty - Decimal('50.0')

def test_multiply(price):
    multiplied_price = price.multiply(Decimal('2.0'))
    assert multiplied_price.qty == price.qty * Decimal('2.0')

def test_times(price):
    times_price = price.times(Decimal('2.0'))
    assert times_price.qty == price.qty * Decimal('2.0')

def test_divide(price):
    divided_price = price.divide(Decimal('2.0'))
    assert divided_price.qty == price.qty / Decimal('2.0')

def test_floor_divide(price):
    floordiv_price = price.floor_divide(Decimal('2.0'))
    assert floordiv_price.qty == price.qty // Decimal('2.0')

def test_lt(price, different_price):
    assert price.lt(different_price) == (price.qty < different_price.qty)

def test_lte(price, different_price):
    assert price.lte(different_price) == (price.qty <= different_price.qty)

def test_gt(price, different_price):
    assert price.gt(different_price) == (price.qty > different_price.qty)

def test_gte(price, different_price):
    assert price.gte(different_price) == (price.qty >= different_price.qty)

def test_with_ccy(price):
    new_ccy = Currency.of('EUR', 'Euro', 2, CurrencyType.MONEY)
    new_price = price.with_ccy(new_ccy)
    assert new_price.ccy == new_ccy

def test_with_qty(price):
    new_qty = Decimal('200.0')
    new_price = price.with_qty(new_qty)
    assert new_price.qty == new_qty

def test_with_dov(price):
    new_dov = Date(2024, 1, 1)
    new_price = price.with_dov(new_dov)
    assert new_price.dov == new_dov

def test_convert(price):
    new_ccy = Currency.of('EUR', 'Euro', 2, CurrencyType.MONEY)
    converted_price = price.convert(new_ccy)
    assert converted_price.ccy == new_ccy

def test_money(price):
    assert price.money == price.qty

def test_bool(price):
    assert bool(price) is True

def test_eq(price, other_price, different_price):
    assert price == other_price
    assert price != different_price

def test_abs(price):
    assert abs(price) == price.abs()

def test_float(price):
    assert float(price) == price.as_float()

def test_int(price):
    assert int(price) == price.as_integer()

def test_round(price):
    assert round(price) == price.round()

def test_neg(price):
    assert -price == price.negative()

def test_pos(price):
    assert +price == price.positive()

def test_add(price, other_price):
    assert price + other_price == price.add(other_price)

def test_sub(price, other_price):
    assert price - other_price == price.subtract(other_price)

def test_mul(price):
    assert price * Decimal('2.0') == price.multiply(Decimal('2.0'))

def test_truediv(price):
    assert price / Decimal('2.0') == price.divide(Decimal('2.0'))

def test_floordiv(price):
    assert price // Decimal('2.0') == price.floor_divide(Decimal('2.0'))

def test_lt(price, different_price):
    assert (price < different_price) == price.lt(different_price)

def test_le(price, different_price):
    assert (price <= different_price) == price.lte(different_price)

def test_gt(price, different_price):
    assert (price > different_price) == price.gt(different_price)

def test_ge(price, different_price):
    assert (price >= different_price) == price.gte(different_price)
