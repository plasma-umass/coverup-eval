# file: pypara/monetary.py:1348-1349
# asked: {"lines": [1348, 1349], "branches": []}
# gained: {"lines": [1348, 1349], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union
from pypara.monetary import NonePrice, Price
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date
from pypara.commons.numbers import Numeric

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

    def round(self, ndigits: int=0) -> 'Price':
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
        return None

    def divide(self, other: Numeric) -> 'Price':
        return self

    def floor_divide(self, other: Numeric) -> 'Price':
        return self

    def lt(self, other: 'Price') -> bool:
        return False

    def lte(self, other: 'Price') -> bool:
        return True

    def gt(self, other: 'Price') -> bool:
        return False

    def gte(self, other: 'Price') -> bool:
        return True

    def with_ccy(self, ccy: Currency) -> 'Price':
        return self

    def with_qty(self, qty: Decimal) -> 'Price':
        return self

    def with_dov(self, dov: Date) -> 'Price':
        return self

    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Price':
        return self

    @property
    def money(self) -> 'Money':
        return None

    @classmethod
    def of(cls, ccy: Optional[Currency], qty: Optional[Decimal], dov: Optional[Date]) -> 'Price':
        return cls()

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

    def __round__(self, ndigits: Optional[int]=0) -> Union['Price', int]:
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
        return True

    def __gt__(self, other: 'Price') -> bool:
        return False

    def __ge__(self, other: 'Price') -> bool:
        return True

@pytest.fixture
def mock_price():
    return MockPrice()

def test_none_price_add(mock_price):
    none_price = NonePrice()
    result = none_price.add(mock_price)
    assert result is mock_price
