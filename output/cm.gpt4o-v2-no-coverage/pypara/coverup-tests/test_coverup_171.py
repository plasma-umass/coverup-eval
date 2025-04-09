# file: pypara/monetary.py:1369-1370
# asked: {"lines": [1369, 1370], "branches": []}
# gained: {"lines": [1369, 1370], "branches": []}

import pytest
from decimal import Decimal
from typing import Optional, Union
from pypara.monetary import NonePrice
from pypara.currencies import Currency
from datetime import date as Date
from pypara.commons.numbers import Numeric
from pypara.monetary import Price
from pypara.monetary import Money

class MockPrice(Price):
    def is_equal(self, other: any) -> bool:
        return False

    def as_boolean(self) -> bool:
        return False

    def as_float(self) -> float:
        return 0.0

    def as_integer(self) -> int:
        return 0

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
        return None

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
    def money(self) -> Money:
        return None

    @classmethod
    def of(cls, ccy: Optional[Currency], qty: Optional[Decimal], dov: Optional[Date]) -> 'Price':
        return cls()

    def __bool__(self) -> bool:
        return False

    def __eq__(self, other: any) -> bool:
        return False

    def __abs__(self) -> 'Price':
        return self

    def __float__(self) -> float:
        return 0.0

    def __int__(self) -> int:
        return 0

    def __round__(self, ndigits: Optional[int] = 0) -> Union['Price', int]:
        return 0

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

@pytest.fixture
def mock_price():
    return MockPrice()

def test_none_price_floor_divide(mock_price):
    none_price = NonePrice()
    result = none_price.floor_divide(mock_price)
    assert result is none_price
