# file: pypara/monetary.py:427-428
# asked: {"lines": [427, 428], "branches": []}
# gained: {"lines": [427], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import NamedTuple
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import Money

class SomeMoney(Money, NamedTuple("SomeMoney", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
    def as_float(self) -> float:
        return self[1].__float__()

def test_some_money_as_float():
    # Arrange
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    quantity = Decimal("123.45")
    date_of_value = Date.today()
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Act
    result = some_money.as_float()
    
    # Assert
    assert result == float(quantity)

