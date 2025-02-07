# file: pypara/monetary.py:119-124
# asked: {"lines": [119, 120, 124], "branches": []}
# gained: {"lines": [119, 120], "branches": []}

import pytest
from abc import abstractmethod
from decimal import Decimal
from typing import Any, Optional, Union, overload
from pypara.commons.numbers import Numeric
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency
from pypara.monetary import Money, MonetaryOperationException

class ConcreteMoney(Money):
    def is_equal(self, other: Any) -> bool:
        return False

    def as_boolean(self) -> bool:
        return False

    def as_float(self) -> float:
        return 0.0

    def as_integer(self) -> int:
        return 0

    def abs(self) -> 'Money':
        return self

    def negative(self) -> 'Money':
        return self

    def positive(self) -> 'Money':
        return self

    def round(self, ndigits: int=0) -> 'Money':
        return self

    def add(self, other: 'Money') -> 'Money':
        return self

    def scalar_add(self, other: Numeric) -> 'Money':
        return self

    def subtract(self, other: 'Money') -> 'Money':
        return self

    def scalar_subtract(self, other: Numeric) -> 'Money':
        return self

    def multiply(self, other: Numeric) -> 'Money':
        return self

    def divide(self, other: Numeric) -> 'Money':
        return self

    def floor_divide(self, other: Numeric) -> 'Money':
        return self

    def lt(self, other: 'Money') -> bool:
        return False

    def lte(self, other: 'Money') -> bool:
        return False

    def gt(self, other: 'Money') -> bool:
        return False

    def gte(self, other: 'Money') -> bool:
        return False

    def with_ccy(self, ccy: Currency) -> 'Money':
        return self

    def with_qty(self, qty: Decimal) -> 'Money':
        return self

    def with_dov(self, dov: Date) -> 'Money':
        return self

    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Money':
        return self

    @property
    def price(self) -> 'Price':
        return self

    def __bool__(self) -> bool:
        return False

    def __eq__(self, other: Any) -> bool:
        return False

    def __abs__(self) -> 'Money':
        return self

    def __float__(self) -> float:
        return 0.0

    def __int__(self) -> int:
        return 0

    def __round__(self, ndigits: Optional[int]=0) -> Union['Money', int]:
        return 0

    def __neg__(self) -> 'Money':
        return self

    def __pos__(self) -> 'Money':
        return self

    def __add__(self, other: 'Money') -> 'Money':
        return self

    def __sub__(self, other: 'Money') -> 'Money':
        return self

    def __mul__(self, other: Numeric) -> 'Money':
        return self

    def __truediv__(self, other: Numeric) -> 'Money':
        return self

    def __floordiv__(self, other: Numeric) -> 'Money':
        return self

    def __lt__(self, other: 'Money') -> bool:
        return False

    def __le__(self, other: 'Money') -> bool:
        return False

    def __gt__(self, other: 'Money') -> bool:
        return False

    def __ge__(self, other: 'Money') -> bool:
        return False

def test_as_integer_not_implemented():
    class IncompleteMoney(Money):
        def is_equal(self, other: Any) -> bool:
            return False

        def as_boolean(self) -> bool:
            return False

        def as_float(self) -> float:
            return 0.0

        def abs(self) -> 'Money':
            return self

        def negative(self) -> 'Money':
            return self

        def positive(self) -> 'Money':
            return self

        def round(self, ndigits: int=0) -> 'Money':
            return self

        def add(self, other: 'Money') -> 'Money':
            return self

        def scalar_add(self, other: Numeric) -> 'Money':
            return self

        def subtract(self, other: 'Money') -> 'Money':
            return self

        def scalar_subtract(self, other: Numeric) -> 'Money':
            return self

        def multiply(self, other: Numeric) -> 'Money':
            return self

        def divide(self, other: Numeric) -> 'Money':
            return self

        def floor_divide(self, other: Numeric) -> 'Money':
            return self

        def lt(self, other: 'Money') -> bool:
            return False

        def lte(self, other: 'Money') -> bool:
            return False

        def gt(self, other: 'Money') -> bool:
            return False

        def gte(self, other: 'Money') -> bool:
            return False

        def with_ccy(self, ccy: Currency) -> 'Money':
            return self

        def with_qty(self, qty: Decimal) -> 'Money':
            return self

        def with_dov(self, dov: Date) -> 'Money':
            return self

        def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Money':
            return self

        @property
        def price(self) -> 'Price':
            return self

        def __bool__(self) -> bool:
            return False

        def __eq__(self, other: Any) -> bool:
            return False

        def __abs__(self) -> 'Money':
            return self

        def __float__(self) -> float:
            return 0.0

        def __int__(self) -> int:
            return 0

        def __round__(self, ndigits: Optional[int]=0) -> Union['Money', int]:
            return 0

        def __neg__(self) -> 'Money':
            return self

        def __pos__(self) -> 'Money':
            return self

        def __add__(self, other: 'Money') -> 'Money':
            return self

        def __sub__(self, other: 'Money') -> 'Money':
            return self

        def __mul__(self, other: Numeric) -> 'Money':
            return self

        def __truediv__(self, other: Numeric) -> 'Money':
            return self

        def __floordiv__(self, other: Numeric) -> 'Money':
            return self

        def __lt__(self, other: 'Money') -> bool:
            return False

        def __le__(self, other: 'Money') -> bool:
            return False

        def __gt__(self, other: 'Money') -> bool:
            return False

        def __ge__(self, other: 'Money') -> bool:
            return False

        @abstractmethod
        def as_integer(self) -> int:
            raise NotImplementedError

    incomplete_money = IncompleteMoney()
    with pytest.raises(NotImplementedError):
        incomplete_money.as_integer()
