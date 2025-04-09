# file: pypara/monetary.py:1327-1328
# asked: {"lines": [1327, 1328], "branches": []}
# gained: {"lines": [1327, 1328], "branches": []}

import pytest
from typing import Any, Optional, Union
from decimal import Decimal
from pypara.commons.numbers import Numeric
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency
from pypara.monetary import NonePrice, Price

class MockPrice(Price):
    def is_equal(self, other: Any) -> bool:
        return isinstance(other, MockPrice)

    def as_boolean(self) -> bool:
        return True

    def as_float(self) -> float:
        return 1.0

    def as_integer(self) -> int:
        return 1

    def abs(self) -> 'Price':
        return self

    def negative(self) -> 'Price':
        return self

    def positive(self) -> 'Price':
        return self

    def round(self, ndigits: int = 0) -> 'Price':
        return self

    def add(self, other: 'Price') -> 'Price':
        return self

    def scalar_add(self, other: Numeric) -> 'Price':
        return self

    def subtract(self, other: 'Price') -> 'Price':
        return self

    def scalar_subtract(self, other: Numeric) -> 'Price':
        return self

    def multiply(self, other: Numeric) -> 'Price':
        return self

    def times(self, other: Numeric) -> 'Money':
        return self

    def divide(self, other: Numeric) -> 'Price':
        return self

    def floor_divide(self, other: Numeric) -> 'Price':
        return self

    def lt(self, other: 'Price') -> bool:
        return False

    def lte(self, other: 'Price') -> bool:
        return False

    def gt(self, other: 'Price') -> bool:
        return False

    def gte(self, other: 'Price') -> bool:
        return False

    def with_ccy(self, ccy: Currency) -> 'Price':
        return self

    def with_qty(self, qty: Decimal) -> 'Price':
        return self

    def with_dov(self, dov: Date) -> 'Price':
        return self

    def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> 'Price':
        return self

    @property
    def money(self) -> 'Money':
        return self

    def __bool__(self) -> bool:
        return True

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, MockPrice)

    def __abs__(self) -> 'Price':
        return self

    def __float__(self) -> float:
        return 1.0

    def __int__(self) -> int:
        return 1

    def __round__(self, ndigits: Optional[int] = 0) -> Union['Price', int]:
        return self

    def __neg__(self) -> 'Price':
        return self

    def __pos__(self) -> 'Price':
        return self

    def __add__(self, other: 'Price') -> 'Price':
        return self

    def __sub__(self, other: 'Price') -> 'Price':
        return self

    def __mul__(self, other: Numeric) -> 'Price':
        return self

    def __truediv__(self, other: Numeric) -> 'Price':
        return self

    def __floordiv__(self, other: Numeric) -> 'Price':
        return self

    def __lt__(self, other: 'Price') -> bool:
        return False

    def __le__(self, other: 'Price') -> bool:
        return False

    def __gt__(self, other: 'Price') -> bool:
        return False

    def __ge__(self, other: 'Price') -> bool:
        return False

def test_noneprice_is_equal():
    none_price = NonePrice()
    mock_price = MockPrice()

    assert none_price.is_equal(NonePrice())
    assert not none_price.is_equal(mock_price)
