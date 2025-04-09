# file: pypara/monetary.py:945-957
# asked: {"lines": [945, 946, 957], "branches": []}
# gained: {"lines": [945, 946], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestPrice(Price):
    def __init__(self, ccy=None, qty=None, dov=None):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.defined = qty is not None
        self.undefined = qty is None

    def gt(self, other):
        if self.undefined:
            return False
        if other.undefined:
            return True
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return self.qty > other.qty

    # Implement other abstract methods with simple pass or return statements
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
    def subtract(self, other): pass
    def scalar_subtract(self, other): pass
    def multiply(self, other): pass
    def times(self, other): pass
    def divide(self, other): pass
    def floor_divide(self, other): pass
    def lt(self, other): pass
    def lte(self, other): pass
    def gte(self, other): pass
    def with_ccy(self, ccy): pass
    def with_qty(self, qty): pass
    def with_dov(self, dov): pass
    def convert(self, to, asof=None, strict=False): pass
    @property
    def money(self): pass
    @classmethod
    def of(cls, ccy, qty, dov): pass
    def __bool__(self): pass
    def __eq__(self, other): pass
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

@pytest.fixture
def price():
    return TestPrice(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("100.00"), dov=Date(2023, 1, 1))

@pytest.fixture
def other_price():
    return TestPrice(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("50.00"), dov=Date(2023, 1, 1))

@pytest.fixture
def undefined_price():
    return TestPrice()

@pytest.fixture
def incompatible_price():
    return TestPrice(ccy=Currency.of("EUR", "Euro", 2, CurrencyType.MONEY), qty=Decimal("100.00"), dov=Date(2023, 1, 1))

def test_gt_defined_vs_undefined(price, undefined_price):
    assert price.gt(undefined_price) is True

def test_gt_undefined_vs_defined(price, undefined_price):
    assert undefined_price.gt(price) is False

def test_gt_defined_vs_defined(price, other_price):
    assert price.gt(other_price) is True
    assert other_price.gt(price) is False

def test_gt_incompatible_currency(price, incompatible_price):
    with pytest.raises(IncompatibleCurrencyError):
        price.gt(incompatible_price)
