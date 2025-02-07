# file: pypara/monetary.py:119-124
# asked: {"lines": [124], "branches": []}
# gained: {"lines": [124], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union, TypeVar
from abc import abstractmethod
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date
from pypara.monetary import Money, MonetaryOperationException

Numeric = TypeVar('Numeric', int, float, Decimal)

class ConcreteMoney(Money):
    def as_integer(self) -> int:
        super().as_integer()

    # Implement other abstract methods with pass or minimal implementation
    def is_equal(self, other: Any) -> bool:
        pass

    def as_boolean(self) -> bool:
        pass

    def as_float(self) -> float:
        pass

    def abs(self) -> 'Money':
        pass

    def negative(self) -> 'Money':
        pass

    def positive(self) -> 'Money':
        pass

    def round(self, ndigits: int=0) -> 'Money':
        pass

    def add(self, other: 'Money') -> 'Money':
        pass

    def scalar_add(self, other: Numeric) -> 'Money':
        pass

    def subtract(self, other: 'Money') -> 'Money':
        pass

    def scalar_subtract(self, other: Numeric) -> 'Money':
        pass

    def multiply(self, other: Numeric) -> 'Money':
        pass

    def divide(self, other: Numeric) -> 'Money':
        pass

    def floor_divide(self, other: Numeric) -> 'Money':
        pass

    def lt(self, other: 'Money') -> bool:
        pass

    def lte(self, other: 'Money') -> bool:
        pass

    def gt(self, other: 'Money') -> bool:
        pass

    def gte(self, other: 'Money') -> bool:
        pass

    def with_ccy(self, ccy: Currency) -> 'Money':
        pass

    def with_qty(self, qty: Decimal) -> 'Money':
        pass

    def with_dov(self, dov: Date) -> 'Money':
        pass

    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Money':
        pass

    @property
    def price(self) -> 'Price':
        pass

    def __bool__(self) -> bool:
        pass

    def __eq__(self, other: Any) -> bool:
        pass

    def __abs__(self) -> 'Money':
        pass

    def __float__(self) -> float:
        pass

    def __int__(self) -> int:
        pass

    def __round__(self, ndigits: Optional[int]=0) -> Union['Money', int]:
        pass

    def __neg__(self) -> 'Money':
        pass

    def __pos__(self) -> 'Money':
        pass

    def __add__(self, other: 'Money') -> 'Money':
        pass

    def __sub__(self, other: 'Money') -> 'Money':
        pass

    def __mul__(self, other: Numeric) -> 'Money':
        pass

    def __truediv__(self, other: Numeric) -> 'Money':
        pass

    def __floordiv__(self, other: Numeric) -> 'Money':
        pass

    def __lt__(self, other: 'Money') -> bool:
        pass

    def __le__(self, other: 'Money') -> bool:
        pass

    def __gt__(self, other: 'Money') -> bool:
        pass

    def __ge__(self, other: 'Money') -> bool:
        pass

def test_as_integer_not_implemented():
    money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        money.as_integer()
