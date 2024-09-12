# file: pypara/monetary.py:227-238
# asked: {"lines": [227, 228, 238], "branches": []}
# gained: {"lines": [227, 228], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union
from pypara.monetary import Money, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from pypara.commons.numbers import Numeric
from pypara.commons.zeitgeist import Date

class TestMoney(Money):
    def __init__(self, ccy, qty, defined=True):
        self.ccy = ccy
        self.qty = qty
        self.defined = defined

    def lt(self, other: "Money") -> bool:
        if not self.defined:
            return other.defined
        if not other.defined:
            return False
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError(self.ccy, other.ccy)
        return self.qty < other.qty

    # Implement other abstract methods with pass or simple return values
    def is_equal(self, other: Any) -> bool: pass
    def as_boolean(self) -> bool: pass
    def as_float(self) -> float: pass
    def as_integer(self) -> int: pass
    def abs(self) -> 'Money': pass
    def negative(self) -> 'Money': pass
    def positive(self) -> 'Money': pass
    def round(self, ndigits: int=0) -> 'Money': pass
    def add(self, other: 'Money') -> 'Money': pass
    def scalar_add(self, other: Numeric) -> 'Money': pass
    def subtract(self, other: 'Money') -> 'Money': pass
    def scalar_subtract(self, other: Numeric) -> 'Money': pass
    def multiply(self, other: Numeric) -> 'Money': pass
    def divide(self, other: Numeric) -> 'Money': pass
    def floor_divide(self, other: Numeric) -> 'Money': pass
    def lte(self, other: 'Money') -> bool: pass
    def gt(self, other: 'Money') -> bool: pass
    def gte(self, other: 'Money') -> bool: pass
    def with_ccy(self, ccy: Currency) -> 'Money': pass
    def with_qty(self, qty: Decimal) -> 'Money': pass
    def with_dov(self, dov: Date) -> 'Money': pass
    def convert(self, to: Currency, asof: Optional[Date]=None, strict: bool=False) -> 'Money': pass
    @property
    def price(self) -> 'Price': pass
    def __bool__(self) -> bool: pass
    def __eq__(self, other: Any) -> bool: pass
    def __abs__(self) -> 'Money': pass
    def __float__(self) -> float: pass
    def __int__(self) -> int: pass
    def __round__(self, ndigits: Optional[int]=0) -> Union['Money', int]: pass
    def __neg__(self) -> 'Money': pass
    def __pos__(self) -> 'Money': pass
    def __add__(self, other: 'Money') -> 'Money': pass
    def __sub__(self, other: 'Money') -> 'Money': pass
    def __mul__(self, other: Numeric) -> 'Money': pass
    def __truediv__(self, other: Numeric) -> 'Money': pass
    def __floordiv__(self, other: Numeric) -> 'Money': pass
    def __lt__(self, other: 'Money') -> bool: pass
    def __le__(self, other: 'Money') -> bool: pass
    def __gt__(self, other: 'Money') -> bool: pass
    def __ge__(self, other: 'Money') -> bool: pass

def test_lt_undefined_money():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money1 = TestMoney(ccy, Decimal("10.00"), defined=False)
    money2 = TestMoney(ccy, Decimal("20.00"), defined=True)
    assert money1.lt(money2) is True

def test_lt_incompatible_currency():
    ccy1 = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    money1 = TestMoney(ccy1, Decimal("10.00"), defined=True)
    money2 = TestMoney(ccy2, Decimal("20.00"), defined=True)
    with pytest.raises(IncompatibleCurrencyError):
        money1.lt(money2)

def test_lt_defined_money():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money1 = TestMoney(ccy, Decimal("10.00"), defined=True)
    money2 = TestMoney(ccy, Decimal("20.00"), defined=True)
    assert money1.lt(money2) is True
    assert money2.lt(money1) is False
