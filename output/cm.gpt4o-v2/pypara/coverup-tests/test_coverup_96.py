# file: pypara/monetary.py:253-265
# asked: {"lines": [253, 254, 265], "branches": []}
# gained: {"lines": [253, 254], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Money, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestMoney(Money):
    def __init__(self, ccy=None, qty=None, dov=None, defined=True):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.defined = defined
        self.undefined = not defined

    def is_equal(self, other):
        return self.qty == other.qty and self.ccy == other.ccy

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return TestMoney(self.ccy, abs(self.qty), self.dov, self.defined)

    def negative(self):
        return TestMoney(self.ccy, -self.qty, self.dov, self.defined)

    def positive(self):
        return TestMoney(self.ccy, +self.qty, self.dov, self.defined)

    def round(self, ndigits=0):
        return TestMoney(self.ccy, round(self.qty, ndigits), self.dov, self.defined)

    def add(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return TestMoney(self.ccy, self.qty + other.qty, self.dov, self.defined)

    def scalar_add(self, other):
        return TestMoney(self.ccy, self.qty + other, self.dov, self.defined)

    def subtract(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return TestMoney(self.ccy, self.qty - other.qty, self.dov, self.defined)

    def scalar_subtract(self, other):
        return TestMoney(self.ccy, self.qty - other, self.dov, self.defined)

    def multiply(self, other):
        return TestMoney(self.ccy, self.qty * other, self.dov, self.defined)

    def divide(self, other):
        return TestMoney(self.ccy, self.qty / other, self.dov, self.defined)

    def floor_divide(self, other):
        return TestMoney(self.ccy, self.qty // other, self.dov, self.defined)

    def lt(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return self.qty < other.qty

    def lte(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return self.qty <= other.qty

    def gt(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        if self.undefined or other.undefined:
            return not self.undefined and other.undefined
        return self.qty > other.qty

    def gte(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return TestMoney(ccy, self.qty, self.dov, self.defined)

    def with_qty(self, qty):
        return TestMoney(self.ccy, qty, self.dov, self.defined)

    def with_dov(self, dov):
        return TestMoney(self.ccy, self.qty, dov, self.defined)

    def convert(self, to, asof=None, strict=False):
        return TestMoney(to, self.qty, asof or self.dov, self.defined)

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
    return TestMoney(currency, Decimal("100.00"), Date.today(), True)

@pytest.fixture
def undefined_money(currency):
    return TestMoney(currency, None, Date.today(), False)

def test_gt_defined_vs_undefined(money, undefined_money):
    assert money.gt(undefined_money) is True

def test_gt_undefined_vs_defined(money, undefined_money):
    assert undefined_money.gt(money) is False

def test_gt_incompatible_currencies(money):
    other_currency = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    other_money = TestMoney(other_currency, Decimal("50.00"), Date.today(), True)
    with pytest.raises(IncompatibleCurrencyError):
        money.gt(other_money)
