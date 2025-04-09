# file: pypara/monetary.py:441-443
# asked: {"lines": [441, 442, 443], "branches": []}
# gained: {"lines": [441, 442, 443], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, Currency, SomeMoney

def test_somemoney_positive():
    # Arrange
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 1, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Act
    positive_money = some_money.positive()
    
    # Assert
    assert positive_money.ccy == currency
    assert positive_money.qty == quantity
    assert positive_money.dov == date_of_value
    assert isinstance(positive_money, SomeMoney)
