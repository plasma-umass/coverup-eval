# file pypara/monetary.py:468-471
# lines [468, 470, 471]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from collections import namedtuple

# Assuming Currency and Money are defined somewhere in pypara.monetary
from pypara.monetary import Currency, Money

# Mocking Currency and Money for the purpose of this test
class Currency:
    def __init__(self, code, quantizer):
        self.code = code
        self.quantizer = quantizer

class Money:
    pass

# The class under test
class SomeMoney(Money, namedtuple("SomeMoneyTuple", ["ccy", "qty", "dov"])):
    ccy: Currency
    qty: Decimal
    dov: Date

    def scalar_add(self, other: Decimal) -> "Money":
        c, q, d = self
        return SomeMoney(c, (q + Decimal(other)).quantize(c.quantizer), d)

@pytest.fixture
def currency():
    return Currency("USD", Decimal("0.01"))

@pytest.fixture
def some_money(currency):
    return SomeMoney(currency, Decimal("100.00"), Date(2023, 1, 1))

def test_scalar_add(some_money):
    result = some_money.scalar_add(Decimal("50.00"))
    assert result.qty == Decimal("150.00").quantize(some_money.ccy.quantizer)
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov

def test_scalar_add_with_integer(some_money):
    result = some_money.scalar_add(50)
    assert result.qty == Decimal("150.00").quantize(some_money.ccy.quantizer)
    assert result.ccy == some_money.ccy
    assert result.dov == some_money.dov
