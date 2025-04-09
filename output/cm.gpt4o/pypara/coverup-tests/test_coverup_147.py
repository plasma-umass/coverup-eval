# file pypara/monetary.py:548-550
# lines [549, 550]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import Money, Currency, Date, SomeMoney

def test_some_money_with_qty():
    # Arrange
    currency = Currency('USD', 2, 'fiat', Decimal('0.01'), Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    new_quantity = Decimal('200.00')
    
    # Act
    new_some_money = some_money.with_qty(new_quantity)
    
    # Assert
    assert new_some_money.ccy == currency
    assert new_some_money.qty == new_quantity.quantize(currency.quantizer)
    assert new_some_money.dov == date_of_value
