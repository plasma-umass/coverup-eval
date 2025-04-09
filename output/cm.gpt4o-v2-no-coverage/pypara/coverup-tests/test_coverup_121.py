# file: pypara/monetary.py:1085-1087
# asked: {"lines": [1085, 1086, 1087], "branches": []}
# gained: {"lines": [1085, 1086], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union
from unittest.mock import Mock
from pypara.monetary import Price
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date
from pypara.commons.numbers import Numeric

class TestPrice(Price):
    def __init__(self, ccy: Currency, qty: Decimal, dov: Date):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov

    def __lt__(self, other: Price) -> bool:
        return self.qty < other.qty

    def is_equal(self, other: Any) -> bool:
        return self.qty == other.qty

    def as_boolean(self) -> bool:
        return bool(self.qty)

    def as_float(self) -> float:
        return float(self.qty)

    def as_integer(self) -> int:
        return int(self.qty)

    def abs(self) -> Price:
        return TestPrice(self.ccy, abs(self.qty), self.dov)

    def negative(self) -> Price:
        return TestPrice(self.ccy, -self.qty, self.dov)

    def positive(self) -> Price:
        return TestPrice(self.ccy, +self.qty, self.dov)

    def round(self, ndigits: int = 0) -> Price:
        return TestPrice(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other: Price) -> Price:
        return TestPrice(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty + other, self.dov)

    def subtract(self, other: Price) -> Price:
        return TestPrice(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty - other, self.dov)

    def multiply(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty * other, self.dov)

    def times(self, other: Numeric) -> 'Money':
        pass

    def divide(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty / other, self.dov)

    def floor_divide(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty // other, self.dov)

    def lt(self, other: Price) -> bool:
        return self.qty < other.qty

    def lte(self, other: Price) -> bool:
        return self.qty <= other.qty

    def gt(self, other: Price) -> bool:
        return self.qty > other.qty

    def gte(self, other: Price) -> bool:
        return self.qty >= other.qty

    def with_ccy(self, ccy: Currency) -> Price:
        return TestPrice(ccy, self.qty, self.dov)

    def with_qty(self, qty: Decimal) -> Price:
        return TestPrice(self.ccy, qty, self.dov)

    def with_dov(self, dov: Date) -> Price:
        return TestPrice(self.ccy, self.qty, dov)

    def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> Price:
        return TestPrice(to, self.qty, asof or self.dov)

    @property
    def money(self) -> 'Money':
        pass

    @classmethod
    def of(cls, ccy: Optional[Currency], qty: Optional[Decimal], dov: Optional[Date]) -> Price:
        return cls(ccy, qty, dov)

    def __bool__(self) -> bool:
        return bool(self.qty)

    def __eq__(self, other: Any) -> bool:
        return self.qty == other.qty

    def __abs__(self) -> Price:
        return TestPrice(self.ccy, abs(self.qty), self.dov)

    def __float__(self) -> float:
        return float(self.qty)

    def __int__(self) -> int:
        return int(self.qty)

    def __round__(self, ndigits: Optional[int] = 0) -> Union[Price, int]:
        return TestPrice(self.ccy, round(self.qty, ndigits), self.dov)

    def __neg__(self) -> Price:
        return TestPrice(self.ccy, -self.qty, self.dov)

    def __pos__(self) -> Price:
        return TestPrice(self.ccy, +self.qty, self.dov)

    def __add__(self, other: Price) -> Price:
        return TestPrice(self.ccy, self.qty + other.qty, self.dov)

    def __sub__(self, other: Price) -> Price:
        return TestPrice(self.ccy, self.qty - other.qty, self.dov)

    def __mul__(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty * other, self.dov)

    def __truediv__(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty / other, self.dov)

    def __floordiv__(self, other: Numeric) -> Price:
        return TestPrice(self.ccy, self.qty // other, self.dov)

    def __le__(self, other: Price) -> bool:
        return self.qty <= other.qty

    def __gt__(self, other: Price) -> bool:
        return self.qty > other.qty

    def __ge__(self, other: Price) -> bool:
        return self.qty >= other.qty

@pytest.fixture
def price():
    ccy = Mock(spec=Currency)
    dov = Mock(spec=Date)
    return TestPrice(ccy, Decimal('100.0'), dov)

@pytest.fixture
def other_price():
    ccy = Mock(spec=Currency)
    dov = Mock(spec=Date)
    return TestPrice(ccy, Decimal('50.0'), dov)

def test_lt(price, other_price):
    assert not price < other_price
    assert other_price < price

def test_eq(price, other_price):
    assert not price == other_price
    assert price == TestPrice(price.ccy, price.qty, price.dov)

def test_add(price, other_price):
    result = price + other_price
    assert result.qty == Decimal('150.0')

def test_sub(price, other_price):
    result = price - other_price
    assert result.qty == Decimal('50.0')

def test_mul(price):
    result = price * 2
    assert result.qty == Decimal('200.0')

def test_truediv(price):
    result = price / 2
    assert result.qty == Decimal('50.0')

def test_floordiv(price):
    result = price // 3
    assert result.qty == Decimal('33.0')
