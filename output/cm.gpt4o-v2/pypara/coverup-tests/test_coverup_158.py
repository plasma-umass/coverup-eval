# file: pypara/monetary.py:909-917
# asked: {"lines": [909, 910, 917], "branches": []}
# gained: {"lines": [909, 910], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric
from typing import Any, Optional, Union
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency
from pypara.monetary import Money

class ConcretePrice(Price):
    def is_equal(self, other: Any) -> bool:
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
        return Money()

    def divide(self, other: Numeric) -> 'Price':
        return self

    def floor_divide(self, other: Numeric) -> 'Price':
        raise NotImplementedError

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

    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Price':
        return self

    @property
    def money(self) -> Money:
        return Money()

    @classmethod
    def of(cls, ccy: Optional[Currency], qty: Optional[Decimal], dov: Optional[Date]) -> 'Price':
        return cls()

    def __bool__(self) -> bool:
        return False

    def __eq__(self, other: Any) -> bool:
        return False

    def __abs__(self) -> 'Price':
        return self

    def __float__(self) -> float:
        return 0.0

    def __int__(self) -> int:
        return 0

    def __round__(self, ndigits: Optional[int]=0) -> Union['Price', int]:
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

def test_floor_divide_not_implemented():
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.floor_divide(10)
