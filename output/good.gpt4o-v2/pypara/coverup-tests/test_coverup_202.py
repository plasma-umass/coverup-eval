# file: pypara/monetary.py:771-781
# asked: {"lines": [781], "branches": []}
# gained: {"lines": [781], "branches": []}

import pytest
from pypara.monetary import Price
from typing import Any
from decimal import Decimal
from pypara.commons.numbers import Numeric
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date
from typing import Optional, Union

def test_price_is_equal_not_implemented():
    class TestPrice(Price):
        def is_equal(self, other: Any) -> bool:
            return super().is_equal(other)
        
        def as_boolean(self) -> bool:
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
        def money(self) -> 'Money':
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

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.is_equal(None)
