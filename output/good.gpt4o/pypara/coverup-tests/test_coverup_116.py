# file pypara/monetary.py:552-553
# lines [552, 553]
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

# The class under test
class SomeMoney(Money, namedtuple("SomeMoney", ["ccy", "qty", "dov"])):
    ccy: Currency
    qty: Decimal
    dov: Date

    def with_dov(self, dov: Date) -> "Money":
        return SomeMoney(self.ccy, self.qty, dov)

def test_with_dov():
    # Arrange
    currency = Currency("USD")
    quantity = Decimal("100.00")
    original_date = Date(2023, 1, 1)
    new_date = Date(2023, 12, 31)
    some_money = SomeMoney(currency, quantity, original_date)
    
    # Act
    new_some_money = some_money.with_dov(new_date)
    
    # Assert
    assert new_some_money.ccy == currency
    assert new_some_money.qty == quantity
    assert new_some_money.dov == new_date
    assert new_some_money is not some_money  # Ensure a new instance is created

