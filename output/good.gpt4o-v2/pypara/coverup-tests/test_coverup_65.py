# file: pypara/monetary.py:531-536
# asked: {"lines": [531, 532, 533, 534, 535, 536], "branches": [[532, 533], [532, 534], [534, 535], [534, 536]]}
# gained: {"lines": [531, 532, 533, 534, 535, 536], "branches": [[532, 533], [532, 534], [534, 535], [534, 536]]}

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
        return self.qty > other.qty

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

@pytest.fixture
def undefined_money(usd):
    return MockMoney(ccy=usd, qty=Decimal("0.00"), undefined=True)

def test_gt_with_undefined_money(some_money_usd, undefined_money):
    assert some_money_usd.gt(undefined_money) is True

def test_gt_with_incompatible_currency(some_money_usd, some_money_eur):
    with pytest.raises(IncompatibleCurrencyError):
        some_money_usd.gt(some_money_eur)

def test_gt_with_compatible_currency(some_money_usd):
    other_money = SomeMoney(ccy=some_money_usd.ccy, qty=Decimal("50.00"), dov=Date.today())
    assert some_money_usd.gt(other_money) is True
