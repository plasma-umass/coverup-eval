# file: pypara/monetary.py:538-543
# asked: {"lines": [538, 539, 540, 541, 542, 543], "branches": [[539, 540], [539, 541], [541, 542], [541, 543]]}
# gained: {"lines": [538, 539, 540, 541, 542, 543], "branches": [[539, 540], [539, 541], [541, 542], [541, 543]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Money, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType

class MockMoney(Money):
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

    def is_equal(self, other):
        return self.qty == other.qty

    def as_boolean(self):
        return bool(self.qty)

    def as_float(self):
        return float(self.qty)

    def as_integer(self):
        return int(self.qty)

    def abs(self):
        return MockMoney(self.ccy, abs(self.qty))

    def negative(self):
        return MockMoney(self.ccy, -self.qty)

    def positive(self):
        return MockMoney(self.ccy, +self.qty)

    def round(self, ndigits=0):
        return MockMoney(self.ccy, round(self.qty, ndigits))

    def add(self, other):
        return MockMoney(self.ccy, self.qty + other.qty)

    def scalar_add(self, other):
        return MockMoney(self.ccy, self.qty + other)

    def subtract(self, other):
        return MockMoney(self.ccy, self.qty - other.qty)

    def scalar_subtract(self, other):
        return MockMoney(self.ccy, self.qty - other)

    def multiply(self, other):
        return MockMoney(self.ccy, self.qty * other)

    def divide(self, other):
        return MockMoney(self.ccy, self.qty / other)

    def floor_divide(self, other):
        return MockMoney(self.ccy, self.qty // other)

    def lt(self, other):
        return self.qty < other.qty

    def lte(self, other):
        return self.qty <= other.qty

    def gt(self, other):
        return self.qty > other.qty

    def gte(self, other):
        return self.qty >= other.qty

    def with_ccy(self, ccy):
        return MockMoney(ccy, self.qty)

    def with_qty(self, qty):
        return MockMoney(self.ccy, qty)

    def with_dov(self, dov):
        return MockMoney(self.ccy, self.qty)

    def convert(self, to, asof=None, strict=False):
        return MockMoney(to, self.qty)

    @property
    def price(self):
        return self.qty

    def __bool__(self):
        return bool(self.qty)

    def __eq__(self, other):
        return self.qty == other.qty

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
def usd():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

@pytest.fixture
def some_money_usd(usd):
    return SomeMoney(ccy=usd, qty=Decimal("100.00"), dov=Date.today())

@pytest.fixture
def some_money_eur(eur):
    return SomeMoney(ccy=eur, qty=Decimal("100.00"), dov=Date.today())

def test_gte_with_undefined_other(some_money_usd):
    other = MockMoney(ccy=some_money_usd.ccy, qty=Decimal("0.00"), undefined=True)
    assert some_money_usd.gte(other) is True

def test_gte_with_different_currency(some_money_usd, some_money_eur):
    with pytest.raises(IncompatibleCurrencyError):
        some_money_usd.gte(some_money_eur)

def test_gte_with_same_currency(some_money_usd):
    other = MockMoney(ccy=some_money_usd.ccy, qty=Decimal("50.00"))
    assert some_money_usd.gte(other) is True
    other = MockMoney(ccy=some_money_usd.ccy, qty=Decimal("150.00"))
    assert some_money_usd.gte(other) is False
