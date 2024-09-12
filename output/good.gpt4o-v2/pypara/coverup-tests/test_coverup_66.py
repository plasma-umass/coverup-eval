# file: pypara/monetary.py:437-439
# asked: {"lines": [437, 438, 439], "branches": []}
# gained: {"lines": [437, 438, 439], "branches": []}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney

def test_somemoney_negative():
    # Arrange
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('100.00')
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Act
    negative_money = some_money.negative()
    
    # Assert
    assert negative_money.ccy == currency
    assert negative_money.qty == -quantity
    assert negative_money.dov == date_of_value
