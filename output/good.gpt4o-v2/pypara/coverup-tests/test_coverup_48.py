# file: pypara/monetary.py:517-522
# asked: {"lines": [517, 518, 519, 520, 521, 522], "branches": [[518, 519], [518, 520], [520, 521], [520, 522]]}
# gained: {"lines": [517, 518, 519, 520, 521, 522], "branches": [[518, 519], [518, 520], [520, 521], [520, 522]]}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Money, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class MockMoney(Money):
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

    def is_equal(self, other):
        pass

    def as_boolean(self):
        pass

    def as_float(self):
        pass

    def as_integer(self):
        pass

    def abs(self):
        pass

    def negative(self):
        pass

    def positive(self):
        pass

    def round(self, ndigits=0):
        pass

    def add(self, other):
        pass

    def scalar_add(self, other):
        pass

    def subtract(self, other):
        pass

    def scalar_subtract(self, other):
        pass

    def multiply(self, other):
        pass

    def divide(self, other):
        pass

    def floor_divide(self, other):
        pass

    def lt(self, other):
        pass

    def lte(self, other):
        pass

    def gt(self, other):
        pass

    def gte(self, other):
        pass

    def with_ccy(self, ccy):
        pass

    def with_qty(self, qty):
        pass

    def with_dov(self, dov):
        pass

    def convert(self, to, asof=None, strict=False):
        pass

    @property
    def price(self):
        pass

    def __bool__(self):
        pass

    def __eq__(self, other):
        pass

    def __abs__(self):
        pass

    def __float__(self):
        pass

    def __int__(self):
        pass

    def __round__(self, ndigits=0):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

@pytest.fixture
def currency():
    return Currency.of(code="USD", name="US Dollar", decimals=2, ctype=CurrencyType.MONEY)

@pytest.fixture
def date():
    return Date(year=2023, month=1, day=1)

@pytest.fixture
def some_money(currency, date):
    return SomeMoney(ccy=currency, qty=Decimal("100.00"), dov=date)

def test_lt_with_undefined_other(some_money, currency, date):
    other = MockMoney(ccy=currency, qty=Decimal("50.00"), undefined=True)
    assert some_money.lt(other) == False

def test_lt_with_incompatible_currency(some_money, date):
    other_currency = Currency.of(code="EUR", name="Euro", decimals=2, ctype=CurrencyType.MONEY)
    other = MockMoney(ccy=other_currency, qty=Decimal("50.00"))
    with pytest.raises(IncompatibleCurrencyError):
        some_money.lt(other)

def test_lt_with_compatible_currency(some_money, currency, date):
    other = MockMoney(ccy=currency, qty=Decimal("50.00"))
    assert some_money.lt(other) == False
    other.qty = Decimal("150.00")
    assert some_money.lt(other) == True
