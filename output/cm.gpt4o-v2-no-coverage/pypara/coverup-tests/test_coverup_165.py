# file: pypara/monetary.py:632-633
# asked: {"lines": [632, 633], "branches": []}
# gained: {"lines": [632, 633], "branches": []}

import pytest
from typing import Any, Optional, Union
from decimal import Decimal
from pypara.commons.numbers import Numeric
from pypara.monetary import NoneMoney, Money
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date

class MockMoney(Money):
    def is_equal(self, other: Any) -> bool:
        return isinstance(other, MockMoney)

    def as_boolean(self) -> bool:
        return True

    def as_float(self) -> float:
        return 1.0

    def as_integer(self) -> int:
        return 1

    def abs(self) -> 'Money':
        return self

    def negative(self) -> 'Money':
        return self

    def positive(self) -> 'Money':
        return self

    def round(self, ndigits: int = 0) -> 'Money':
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

    def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> 'Money':
        return self

    @property
    def price(self) -> 'Price':
        return self

    def __bool__(self) -> bool:
        return True

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, MockMoney)

    def __abs__(self) -> 'Money':
        return self

    def __float__(self) -> float:
        return 1.0

    def __int__(self) -> int:
        return 1

    def __round__(self, ndigits: Optional[int] = 0) -> Union['Money', int]:
        return self

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

@pytest.fixture
def mock_money():
    return MockMoney()

@pytest.fixture
def none_money():
    return NoneMoney()

def test_none_money_is_equal_with_none_money(none_money):
    assert none_money.is_equal(NoneMoney())

def test_none_money_is_equal_with_mock_money(none_money, mock_money):
    assert not none_money.is_equal(mock_money)
