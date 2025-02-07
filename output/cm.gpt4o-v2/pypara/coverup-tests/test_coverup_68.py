# file: pypara/monetary.py:433-435
# asked: {"lines": [433, 434, 435], "branches": []}
# gained: {"lines": [433, 434, 435], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_somemoney_abs():
    # Arrange
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('-100.00')
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Act
    result = some_money.abs()
    
    # Assert
    assert result.ccy == currency
    assert result.qty == abs(quantity)
    assert result.dov == date_of_value
