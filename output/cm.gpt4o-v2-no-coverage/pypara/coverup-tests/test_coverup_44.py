# file: pypara/monetary.py:517-522
# asked: {"lines": [517, 518, 519, 520, 521, 522], "branches": [[518, 519], [518, 520], [520, 521], [520, 522]]}
# gained: {"lines": [517, 518, 519, 520, 521, 522], "branches": [[518, 519], [518, 520], [520, 521], [520, 522]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney, IncompatibleCurrencyError, Money

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

    @classmethod
    def of(cls, ccy, qty, dov):
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
def mock_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def other_currency():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

@pytest.fixture
def some_money(mock_currency):
    return SomeMoney(ccy=mock_currency, qty=Decimal("100.00"), dov=Date(2023, 1, 1))

@pytest.fixture
def other_money(mock_currency):
    return MockMoney(ccy=mock_currency, qty=Decimal("50.00"))

@pytest.fixture
def incompatible_money(other_currency):
    return MockMoney(ccy=other_currency, qty=Decimal("50.00"))

@pytest.fixture
def undefined_money(mock_currency):
    return MockMoney(ccy=mock_currency, qty=Decimal("50.00"), undefined=True)

def test_lt_undefined(some_money, undefined_money):
    assert some_money.lt(undefined_money) == False

def test_lt_incompatible_currency(some_money, incompatible_money):
    with pytest.raises(IncompatibleCurrencyError):
        some_money.lt(incompatible_money)

def test_lt_comparison(some_money, other_money):
    assert some_money.lt(other_money) == False
    other_money.qty = Decimal("150.00")
    assert some_money.lt(other_money) == True
