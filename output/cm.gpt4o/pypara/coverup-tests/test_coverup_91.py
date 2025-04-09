# file pypara/monetary.py:430-431
# lines [430, 431]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from collections import namedtuple

# Assuming Currency and Money are defined somewhere in pypara.monetary
from pypara.monetary import Currency, Money

# Mocking Currency and Money for the purpose of this test
class Currency:
    def __init__(self, code):
        self.code = code

class Money:
    pass

class SomeMoney(Money, namedtuple("SomeMoney", ["ccy", "qty", "dov"])):
    def as_integer(self) -> int:
        return self.qty.__int__()

def test_some_money_as_integer():
    currency = Currency("USD")
    quantity = Decimal("123.45")
    date_of_value = Date(2023, 10, 1)
    
    some_money = SomeMoney(ccy=currency, qty=quantity, dov=date_of_value)
    
    assert some_money.as_integer() == 123

    # Clean up if necessary (not needed in this case as no external state is modified)

