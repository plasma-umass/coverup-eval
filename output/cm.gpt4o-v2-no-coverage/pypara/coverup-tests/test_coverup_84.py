# file: pypara/monetary.py:1192-1194
# asked: {"lines": [1192, 1193, 1194], "branches": []}
# gained: {"lines": [1192, 1193, 1194], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date
from pypara.monetary import SomeMoney

def test_someprice_times():
    # Setup
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('100.00')
    date_of_value = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date_of_value)
    
    # Test
    result = some_price.times(2)
    
    # Assert
    expected_quantity = (quantity * Decimal(2)).quantize(currency.quantizer)
    expected_result = SomeMoney(currency, expected_quantity, date_of_value)
    assert result == expected_result
