# file: pypara/monetary.py:838-849
# asked: {"lines": [838, 839, 849], "branches": []}
# gained: {"lines": [838, 839, 849], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date
from decimal import Decimal
from typing import Any

class TestPrice(Price):
    def __init__(self, ccy: Currency, qty: Decimal, dov: Date):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.undefined = False

    def is_equal(self, other: Any) -> bool:
        return isinstance(other, TestPrice) and self.ccy == other.ccy and self.qty == other.qty

    def as_boolean(self) -> bool:
        return bool(self.qty)

    def as_float(self) -> float:
        return float(self.qty)

    def as_integer(self) -> int:
        return int(self.qty)

    def abs(self) -> 'Price':
        return TestPrice(self.ccy, abs(self.qty), self.dov)

    def negative(self) -> 'Price':
        return TestPrice(self.ccy, -self.qty, self.dov)

    def positive(self) -> 'Price':
        return TestPrice(self.ccy, +self.qty, self.dov)

    def round(self, ndigits: int=0) -> 'Price':
        return TestPrice(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other: 'Price') -> 'Price':
        if not isinstance(other, TestPrice):
            raise TypeError("Incompatible type for addition")
        if self.ccy != other.ccy:
            raise ValueError("IncompatibleCurrencyError")
        if self.undefined:
            return other
        if other.undefined:
            return self
        return TestPrice(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other: Decimal) -> 'Price':
        return TestPrice(self.ccy, self.qty + other, self.dov)

    def subtract(self, other: 'Price') -> 'Price':
        if not isinstance(other, TestPrice):
            raise TypeError("Incompatible type for subtraction")
        if self.ccy != other.ccy:
            raise ValueError("IncompatibleCurrencyError")
        return TestPrice(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other: Decimal) -> 'Price':
        return TestPrice(self.ccy, self.qty - other, self.dov)

    def multiply(self, other: Decimal) -> 'Price':
        return TestPrice(self.ccy, self.qty * other, self.dov)

    def times(self, other: Decimal) -> 'Money':
        pass

    def divide(self, other: Decimal) -> 'Price':
        return TestPrice(self.ccy, self.qty / other, self.dov)

    def floor_divide(self, other: Decimal) -> 'Price':
        return TestPrice(self.ccy, self.qty // other, self.dov)

    def lt(self, other: 'Price') -> bool:
        return self.qty < other.qty

    def lte(self, other: 'Price') -> bool:
        return self.qty <= other.qty

    def gt(self, other: 'Price') -> bool:
        return self.qty > other.qty

    def gte(self, other: 'Price') -> bool:
        return self.qty >= other.qty

    def with_ccy(self, ccy: Currency) -> 'Price':
        return TestPrice(ccy, self.qty, self.dov)

    def with_qty(self, qty: Decimal) -> 'Price':
        return TestPrice(self.ccy, qty, self.dov)

    def with_dov(self, dov: Date) -> 'Price':
        return TestPrice(self.ccy, self.qty, dov)

    def convert(self, to: Currency, asof: Date=None, strict: bool=False) -> 'Price':
        return TestPrice(to, self.qty, self.dov)

    @property
    def money(self) -> 'Money':
        pass

    @classmethod
    def of(cls, ccy: Currency, qty: Decimal, dov: Date) -> 'Price':
        return cls(ccy, qty, dov)

    def __bool__(self) -> bool:
        return bool(self.qty)

    def __eq__(self, other: Any) -> bool:
        return self.is_equal(other)

    def __abs__(self) -> 'Price':
        return self.abs()

    def __float__(self) -> float:
        return self.as_float()

    def __int__(self) -> int:
        return self.as_integer()

    def __round__(self, ndigits: int=0) -> 'Price':
        return self.round(ndigits)

    def __neg__(self) -> 'Price':
        return self.negative()

    def __pos__(self) -> 'Price':
        return self.positive()

    def __add__(self, other: 'Price') -> 'Price':
        return self.add(other)

    def __sub__(self, other: 'Price') -> 'Price':
        return self.subtract(other)

    def __mul__(self, other: Decimal) -> 'Price':
        return self.multiply(other)

    def __truediv__(self, other: Decimal) -> 'Price':
        return self.divide(other)

    def __floordiv__(self, other: Decimal) -> 'Price':
        return self.floor_divide(other)

    def __lt__(self, other: 'Price') -> bool:
        return self.lt(other)

    def __le__(self, other: 'Price') -> bool:
        return self.lte(other)

    def __gt__(self, other: 'Price') -> bool:
        return self.gt(other)

    def __ge__(self, other: 'Price') -> bool:
        return self.gte(other)

@pytest.fixture
def price():
    return TestPrice(Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), Decimal("100.00"), Date(2023, 1, 1))

@pytest.fixture
def other_price():
    return TestPrice(Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), Decimal("50.00"), Date(2023, 1, 1))

@pytest.fixture
def incompatible_price():
    return TestPrice(Currency.of("EUR", "Euro", 2, CurrencyType.MONEY), Decimal("50.00"), Date(2023, 1, 1))

def test_add(price, other_price):
    result = price.add(other_price)
    assert result.qty == Decimal("150.00")
    assert result.ccy == price.ccy
    assert result.dov == price.dov

def test_add_incompatible_currency(price, incompatible_price):
    with pytest.raises(ValueError, match="IncompatibleCurrencyError"):
        price.add(incompatible_price)

def test_add_undefined(price):
    price.undefined = True
    other_price = TestPrice(Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), Decimal("50.00"), Date(2023, 1, 1))
    result = price.add(other_price)
    assert result == other_price

def test_add_other_undefined(price):
    other_price = TestPrice(Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), Decimal("50.00"), Date(2023, 1, 1))
    other_price.undefined = True
    result = price.add(other_price)
    assert result == price

def test_add_not_implemented():
    with pytest.raises(NotImplementedError):
        Price.add(None, None)
