# file pypara/monetary.py:433-435
# lines [434, 435]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, Currency, SomeMoney

def test_somemoney_abs():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, "fiat", Decimal("0.01"), None)
    quantity = Decimal("-100.00")
    date_of_value = Date(2023, 1, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Act
    abs_money = some_money.abs()
    
    # Assert
    assert abs_money.ccy == currency
    assert abs_money.qty == abs(quantity)
    assert abs_money.dov == date_of_value
