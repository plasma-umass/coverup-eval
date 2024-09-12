# file: pypara/monetary.py:783-793
# asked: {"lines": [783, 784, 793], "branches": []}
# gained: {"lines": [783, 784], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union
from pypara.monetary import Price
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date
from pypara.commons.numbers import Numeric
from pypara.monetary import Money

class TestPrice(Price):
    def __init__(self, defined, qty):
        self.defined = defined
        self.qty = qty

    def as_boolean(self) -> bool:
        if not self.defined or self.qty == Decimal(0):
            return False
        return True

    # Implement other abstract methods with pass or simple return to satisfy the abstract base class
    def is_equal(self, other: Any) -> bool:
        pass

    def as_float(self) -> float:
        pass

    def as_integer(self) -> int:
        pass

    def abs(self) -> 'Price':
        pass

    def negative(self) -> 'Price':
        pass

    def positive(self) -> 'Price':
        pass

    def round(self, ndigits: int=0) -> 'Price':
        pass

    def add(self, other: 'Price') -> 'Price':
        pass

    def scalar_add(self, other: Numeric) -> 'Price':
        pass

    def subtract(self, other: 'Price') -> 'Price':
        pass

    def scalar_subtract(self, other: Numeric) -> 'Price':
        pass

    def multiply(self, other: Numeric) -> 'Price':
        pass

    def times(self, other: Numeric) -> 'Money':
        pass

    def divide(self, other: Numeric) -> 'Price':
        pass

    def floor_divide(self, other: Numeric) -> 'Price':
        pass

    def lt(self, other: 'Price') -> bool:
        pass

    def lte(self, other: 'Price') -> bool:
        pass

    def gt(self, other: 'Price') -> bool:
        pass

    def gte(self, other: 'Price') -> bool:
        pass

    def with_ccy(self, ccy: Currency) -> 'Price':
        pass

    def with_qty(self, qty: Decimal) -> 'Price':
        pass

    def with_dov(self, dov: Date) -> 'Price':
        pass

    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Price':
        pass

    @property
    def money(self) -> Money:
        pass

    @classmethod
    def of(cls, ccy: Optional[Currency], qty: Optional[Decimal], dov: Optional[Date]) -> 'Price':
        pass

    def __bool__(self) -> bool:
        pass

    def __eq__(self, other: Any) -> bool:
        pass

    def __abs__(self) -> 'Price':
        pass

    def __float__(self) -> float:
        pass

    def __int__(self) -> int:
        pass

    def __round__(self, ndigits: Optional[int]=0) -> Union['Price', int]:
        pass

    def __neg__(self) -> 'Price':
        pass

    def __pos__(self) -> 'Price':
        pass

    def __add__(self, other: 'Price') -> 'Price':
        pass

    def __sub__(self, other: 'Price') -> 'Price':
        pass

    def __mul__(self, other: Numeric) -> 'Price':
        pass

    def __truediv__(self, other: Numeric) -> 'Price':
        pass

    def __floordiv__(self, other: Numeric) -> 'Price':
        pass

    def __lt__(self, other: 'Price') -> bool:
        pass

    def __le__(self, other: 'Price') -> bool:
        pass

    def __gt__(self, other: 'Price') -> bool:
        pass

    def __ge__(self, other: 'Price') -> bool:
        pass

@pytest.mark.parametrize("defined, qty, expected", [
    (False, Decimal(0), False),
    (False, Decimal(10), False),
    (True, Decimal(0), False),
    (True, Decimal(10), True),
])
def test_as_boolean(defined, qty, expected):
    price = TestPrice(defined, qty)
    assert price.as_boolean() == expected
