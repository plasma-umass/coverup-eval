# file: pypara/monetary.py:1005-1011
# asked: {"lines": [1005, 1006, 1007, 1011], "branches": []}
# gained: {"lines": [1005, 1006, 1007, 1011], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union
from pypara.monetary import Price, Money
from pypara.currencies import Currency
from pypara.commons.numbers import Numeric
from pypara.commons.zeitgeist import Date

def test_price_money_not_implemented():
    class TestPrice(Price):
        @property
        def money(self) -> Money:
            return super().money

    with pytest.raises(NotImplementedError):
        TestPrice().money

def test_price_money_property():
    class TestMoney(Money):
        def __init__(self, amount, currency):
            self.amount = amount
            self.currency = currency

        def is_equal(self, other: Any) -> bool:
            return self.amount == other.amount and self.currency == other.currency

        def as_boolean(self) -> bool:
            return bool(self.amount)

        def as_float(self) -> float:
            return float(self.amount)

        def as_integer(self) -> int:
            return int(self.amount)

        def abs(self) -> 'Money':
            return TestMoney(abs(self.amount), self.currency)

        def negative(self) -> 'Money':
            return TestMoney(-self.amount, self.currency)

        def positive(self) -> 'Money':
            return TestMoney(+self.amount, self.currency)

        def round(self, ndigits: int=0) -> 'Money':
            return TestMoney(round(self.amount, ndigits), self.currency)

        def add(self, other: 'Money') -> 'Money':
            return TestMoney(self.amount + other.amount, self.currency)

        def scalar_add(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount + other, self.currency)

        def subtract(self, other: 'Money') -> 'Money':
            return TestMoney(self.amount - other.amount, self.currency)

        def scalar_subtract(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount - other, self.currency)

        def multiply(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount * other, self.currency)

        def divide(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount / other, self.currency)

        def floor_divide(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount // other, self.currency)

        def lt(self, other: 'Money') -> bool:
            return self.amount < other.amount

        def lte(self, other: 'Money') -> bool:
            return self.amount <= other.amount

        def gt(self, other: 'Money') -> bool:
            return self.amount > other.amount

        def gte(self, other: 'Money') -> bool:
            return self.amount >= other.amount

        def with_ccy(self, ccy: Currency) -> 'Money':
            return TestMoney(self.amount, ccy)

        def with_qty(self, qty: Decimal) -> 'Money':
            return TestMoney(qty, self.currency)

        def with_dov(self, dov: Date) -> 'Money':
            return self

        def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Money':
            return TestMoney(self.amount, to)

        @property
        def price(self) -> 'Price':
            return self

        def __bool__(self) -> bool:
            return bool(self.amount)

        def __eq__(self, other: Any) -> bool:
            return self.amount == other.amount and self.currency == other.currency

        def __abs__(self) -> 'Money':
            return TestMoney(abs(self.amount), self.currency)

        def __float__(self) -> float:
            return float(self.amount)

        def __int__(self) -> int:
            return int(self.amount)

        def __round__(self, ndigits: Optional[int]=0) -> Union['Money', int]:
            return TestMoney(round(self.amount, ndigits), self.currency)

        def __neg__(self) -> 'Money':
            return TestMoney(-self.amount, self.currency)

        def __pos__(self) -> 'Money':
            return TestMoney(+self.amount, self.currency)

        def __add__(self, other: 'Money') -> 'Money':
            return TestMoney(self.amount + other.amount, self.currency)

        def __sub__(self, other: 'Money') -> 'Money':
            return TestMoney(self.amount - other.amount, self.currency)

        def __mul__(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount * other, self.currency)

        def __truediv__(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount / other, self.currency)

        def __floordiv__(self, other: Numeric) -> 'Money':
            return TestMoney(self.amount // other, self.currency)

        def __lt__(self, other: 'Money') -> bool:
            return self.amount < other.amount

        def __le__(self, other: 'Money') -> bool:
            return self.amount <= other.amount

        def __gt__(self, other: 'Money') -> bool:
            return self.amount > other.amount

        def __ge__(self, other: 'Money') -> bool:
            return self.amount >= other.amount

    class TestPrice(Price):
        @property
        def money(self) -> Money:
            return TestMoney(100, 'USD')

    price = TestPrice()
    assert price.money.amount == 100
    assert price.money.currency == 'USD'
