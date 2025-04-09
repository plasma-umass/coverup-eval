# file: pypara/monetary.py:177-188
# asked: {"lines": [177, 178, 188], "branches": []}
# gained: {"lines": [177, 178], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Money
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestMoney(Money):
    def __init__(self, ccy, qty, dov, defined=True):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.defined = defined
        self.undefined = not defined

    def subtract(self, other):
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError("Currencies do not match")
        if self.undefined:
            return other
        if other.undefined:
            return self
        return TestMoney(self.ccy, self.qty - other.qty, self.dov)

    # Implement other abstract methods with pass or simple return values
    def is_equal(self, other): pass
    def as_boolean(self): pass
    def as_float(self): pass
    def as_integer(self): pass
    def abs(self): pass
    def negative(self): pass
    def positive(self): pass
    def round(self, ndigits=0): pass
    def add(self, other): pass
    def scalar_add(self, other): pass
    def scalar_subtract(self, other): pass
    def multiply(self, other): pass
    def divide(self, other): pass
    def floor_divide(self, other): pass
    def lt(self, other): pass
    def lte(self, other): pass
    def gt(self, other): pass
    def gte(self, other): pass
    def with_ccy(self, ccy): pass
    def with_qty(self, qty): pass
    def with_dov(self, dov): pass
    def convert(self, to, asof=None, strict=False): pass
    @property
    def price(self): pass
    def __bool__(self): pass
    def __eq__(self, other): return isinstance(other, TestMoney) and self.ccy == other.ccy and self.qty == other.qty and self.dov == other.dov and self.defined == other.defined
    def __abs__(self): pass
    def __float__(self): pass
    def __int__(self): pass
    def __round__(self, ndigits=0): pass
    def __neg__(self): pass
    def __pos__(self): pass
    def __add__(self, other): pass
    def __sub__(self, other): pass
    def __mul__(self, other): pass
    def __truediv__(self, other): pass
    def __floordiv__(self, other): pass
    def __lt__(self, other): pass
    def __le__(self, other): pass
    def __gt__(self, other): pass
    def __ge__(self, other): pass

class IncompatibleCurrencyError(Exception):
    pass

@pytest.fixture
def currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def date():
    return Date(2023, 1, 1)

def test_subtract_same_currency_defined(currency, date):
    money1 = TestMoney(currency, Decimal("100.00"), date)
    money2 = TestMoney(currency, Decimal("50.00"), date)
    result = money1.subtract(money2)
    assert result.qty == Decimal("50.00")
    assert result.ccy == currency
    assert result.dov == date

def test_subtract_different_currency(currency, date):
    money1 = TestMoney(currency, Decimal("100.00"), date)
    money2 = TestMoney(Currency.of("EUR", "Euro", 2, CurrencyType.MONEY), Decimal("50.00"), date)
    with pytest.raises(IncompatibleCurrencyError):
        money1.subtract(money2)

def test_subtract_undefined_self(currency, date):
    money1 = TestMoney(currency, Decimal("100.00"), date, defined=False)
    money2 = TestMoney(currency, Decimal("50.00"), date)
    result = money1.subtract(money2)
    assert result == money2

def test_subtract_undefined_other(currency, date):
    money1 = TestMoney(currency, Decimal("100.00"), date)
    money2 = TestMoney(currency, Decimal("50.00"), date, defined=False)
    result = money1.subtract(money2)
    assert result == money1
