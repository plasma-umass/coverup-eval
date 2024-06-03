# file pypara/monetary.py:441-443
# lines [442, 443]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, Currency, SomeMoney

def test_some_money_positive():
    # Arrange
    currency = Currency("USD", "United States Dollar", 2, Decimal('0.01'), None, None)
    quantity = Decimal("-100.00")
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Act
    positive_money = some_money.positive()
    
    # Assert
    assert positive_money.ccy == currency
    assert positive_money.qty == quantity.__pos__()
    assert positive_money.dov == date_of_value
