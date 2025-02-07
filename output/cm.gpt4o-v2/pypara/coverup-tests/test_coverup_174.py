# file: pypara/monetary.py:1065-1067
# asked: {"lines": [1065, 1066, 1067], "branches": []}
# gained: {"lines": [1065, 1066], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date
from typing import Any, Optional, Union
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def __init__(self, ccy: Currency, qty: Decimal, dov: Date):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov

    def is_equal(self, other: Any) -> bool:
        return isinstance(other, Price) and self.ccy == other.ccy and self.qty == other.qty and self.dov == other.dov

    def as_boolean(self) -> bool:
        return bool(self.qty)

    def as_float(self) -> float:
        return float(self.qty)

    def as_integer(self) -> int:
        return int(self.qty)

    def abs(self) -> 'Price':
        return self if self.qty >= 0 else ConcretePrice(self.ccy, -self.qty, self.dov)

    def negative(self) -> 'Price':
        return ConcretePrice(self.ccy, -self.qty, self.dov)

    def positive(self) -> 'Price':
        return self

    def round(self, ndigits: int=0) -> 'Price':
        return ConcretePrice(self.ccy, round(self.qty, ndigits), self.dov)

    def add(self, other: 'Price') -> 'Price':
        return ConcretePrice(self.ccy, self.qty + other.qty, self.dov)

    def scalar_add(self, other: Numeric) -> 'Price':
        return ConcretePrice(self.ccy, self.qty + Decimal(other), self.dov)

    def subtract(self, other: 'Price') -> 'Price':
        return ConcretePrice(self.ccy, self.qty - other.qty, self.dov)

    def scalar_subtract(self, other: Numeric) -> 'Price':
        return ConcretePrice(self.ccy, self.qty - Decimal(other), self.dov)

    def multiply(self, other: Numeric) -> 'Price':
        return ConcretePrice(self.ccy, self.qty * Decimal(other), self.dov)

    def times(self, other: Numeric) -> 'Money':
        pass

    def divide(self, other: Numeric) -> 'Price':
        return ConcretePrice(self.ccy, self.qty / Decimal(other), self.dov)

    def floor_divide(self, other: Numeric) -> 'Price':
        return ConcretePrice(self.ccy, self.qty // Decimal(other), self.dov)

    def lt(self, other: 'Price') -> bool:
        return self.qty < other.qty

    def lte(self, other: 'Price') -> bool:
        return self.qty <= other.qty

    def gt(self, other: 'Price') -> bool:
        return self.qty > other.qty

    def gte(self, other: 'Price') -> bool:
        return self.qty >= other.qty

    def with_ccy(self, ccy: Currency) -> 'Price':
        return ConcretePrice(ccy, self.qty, self.dov)

    def with_qty(self, qty: Decimal) -> 'Price':
        return ConcretePrice(self.ccy, qty, self.dov)

    def with_dov(self, dov: Date) -> 'Price':
        return ConcretePrice(self.ccy, self.qty, dov)

    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Price':
        pass

    @property
    def money(self) -> 'Money':
        pass

    @classmethod
    def of(cls, ccy: Optional[Currency], qty: Optional[Decimal], dov: Optional[Date]) -> 'Price':
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

    def __round__(self, ndigits: Optional[int]=0) -> Union['Price', int]:
        return self.round(ndigits)

    def __neg__(self) -> 'Price':
        return self.negative()

    def __pos__(self) -> 'Price':
        return self.positive()

    def __add__(self, other: 'Price') -> 'Price':
        return self.add(other)

    def __sub__(self, other: 'Price') -> 'Price':
        return self.subtract(other)

    def __mul__(self, other: Numeric) -> 'Price':
        return self.multiply(other)

    def __truediv__(self, other: Numeric) -> 'Price':
        return self.divide(other)

    def __floordiv__(self, other: Numeric) -> 'Price':
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
    return ConcretePrice(Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY), Decimal('100.0'), Date(2023, 1, 1))

def test_price_addition(price):
    other_price = ConcretePrice(Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY), Decimal('50.0'), Date(2023, 1, 1))
    result = price + other_price
    assert result.qty == Decimal('150.0')
    assert result.ccy == price.ccy
    assert result.dov == price.dov
