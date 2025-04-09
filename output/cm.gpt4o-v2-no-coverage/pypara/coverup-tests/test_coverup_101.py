# file: pypara/monetary.py:240-251
# asked: {"lines": [240, 241, 251], "branches": []}
# gained: {"lines": [240, 241], "branches": []}

import pytest
from decimal import Decimal
from typing import Any, Optional, Union
from pypara.monetary import Money
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date
from pypara.commons.numbers import Numeric

class TestMoney(Money):
    def __init__(self, ccy=None, qty=None, dov=None, defined=True):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.defined = defined
        self.undefined = not defined

    def lte(self, other: "Money") -> bool:
        if self.undefined:
            return True
        if other.undefined:
            return False
        if self.ccy != other.ccy:
            raise IncompatibleCurrencyError("Currencies do not match")
        return self.qty <= other.qty

    # Implement other abstract methods with simple pass or return statements
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
    def lt(self, other: 'Money') -> bool: pass
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

class IncompatibleCurrencyError(Exception):
    pass

def test_lte_undefined_self():
    money1 = TestMoney(defined=False)
    money2 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    assert money1.lte(money2) == True

def test_lte_undefined_other():
    money1 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    money2 = TestMoney(defined=False)
    assert money1.lte(money2) == False

def test_lte_incompatible_currency():
    money1 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    money2 = TestMoney(ccy=Currency.of("EUR", "Euro", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    with pytest.raises(IncompatibleCurrencyError):
        money1.lte(money2)

def test_lte_less_than():
    money1 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("5.00"))
    money2 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    assert money1.lte(money2) == True

def test_lte_equal():
    money1 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    money2 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    assert money1.lte(money2) == True

def test_lte_greater_than():
    money1 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("15.00"))
    money2 = TestMoney(ccy=Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), qty=Decimal("10.00"))
    assert money1.lte(money2) == False
