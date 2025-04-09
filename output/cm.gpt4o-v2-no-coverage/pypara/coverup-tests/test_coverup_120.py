# file: pypara/monetary.py:830-836
# asked: {"lines": [830, 831, 836], "branches": []}
# gained: {"lines": [830, 831], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union
from pypara.monetary import Price
from pypara.commons.numbers import Numeric
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency
from unittest.mock import Mock

class TestPrice(Price):
    def __init__(self, qty):
        self.qty = qty

    def round(self, ndigits: int = 0) -> "Price":
        return TestPrice(round(self.qty, ndigits))

    def is_equal(self, other: Any) -> bool:
        return self.qty == other.qty

    def as_boolean(self) -> bool:
        return bool(self.qty)

    def as_float(self) -> float:
        return float(self.qty)

    def as_integer(self) -> int:
        return int(self.qty)

    def abs(self) -> 'Price':
        return TestPrice(abs(self.qty))

    def negative(self) -> 'Price':
        return TestPrice(-self.qty)

    def positive(self) -> 'Price':
        return TestPrice(+self.qty)

    def add(self, other: 'Price') -> 'Price':
        return TestPrice(self.qty + other.qty)

    def scalar_add(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty + other)

    def subtract(self, other: 'Price') -> 'Price':
        return TestPrice(self.qty - other.qty)

    def scalar_subtract(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty - other)

    def multiply(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty * other)

    def times(self, other: Numeric) -> 'Money':
        pass

    def divide(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty / other)

    def floor_divide(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty // other)

    def lt(self, other: 'Price') -> bool:
        return self.qty < other.qty

    def lte(self, other: 'Price') -> bool:
        return self.qty <= other.qty

    def gt(self, other: 'Price') -> bool:
        return self.qty > other.qty

    def gte(self, other: 'Price') -> bool:
        return self.qty >= other.qty

    def with_ccy(self, ccy: Currency) -> 'Price':
        pass

    def with_qty(self, qty: Decimal) -> 'Price':
        return TestPrice(qty)

    def with_dov(self, dov: Date) -> 'Price':
        pass

    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Price':
        pass

    @property
    def money(self) -> 'Money':
        pass

    @classmethod
    def of(cls, ccy: Optional[Currency], qty: Optional[Decimal], dov: Optional[Date]) -> 'Price':
        return cls(qty)

    def __bool__(self) -> bool:
        return bool(self.qty)

    def __eq__(self, other: Any) -> bool:
        return self.qty == other.qty

    def __abs__(self) -> 'Price':
        return TestPrice(abs(self.qty))

    def __float__(self) -> float:
        return float(self.qty)

    def __int__(self) -> int:
        return int(self.qty)

    def __round__(self, ndigits: Optional[int]=0) -> Union['Price', int]:
        return TestPrice(round(self.qty, ndigits))

    def __neg__(self) -> 'Price':
        return TestPrice(-self.qty)

    def __pos__(self) -> 'Price':
        return TestPrice(+self.qty)

    def __add__(self, other: 'Price') -> 'Price':
        return TestPrice(self.qty + other.qty)

    def __sub__(self, other: 'Price') -> 'Price':
        return TestPrice(self.qty - other.qty)

    def __mul__(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty * other)

    def __truediv__(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty / other)

    def __floordiv__(self, other: Numeric) -> 'Price':
        return TestPrice(self.qty // other)

    def __lt__(self, other: 'Price') -> bool:
        return self.qty < other.qty

    def __le__(self, other: 'Price') -> bool:
        return self.qty <= other.qty

    def __gt__(self, other: 'Price') -> bool:
        return self.qty > other.qty

    def __ge__(self, other: 'Price') -> bool:
        return self.qty >= other.qty

def test_round():
    price = TestPrice(Decimal('2.555'))
    rounded_price = price.round(2)
    assert rounded_price.qty == Decimal('2.56')

    rounded_price = price.round(0)
    assert rounded_price.qty == Decimal('3')
