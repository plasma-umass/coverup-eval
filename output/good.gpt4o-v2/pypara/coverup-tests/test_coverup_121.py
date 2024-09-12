# file: pypara/monetary.py:427-428
# asked: {"lines": [427, 428], "branches": []}
# gained: {"lines": [427, 428], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_as_float():
    # Create a SomeMoney instance
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('123.45')
    date_of_value = Date(2023, 10, 1)
    money_instance = SomeMoney(currency, quantity, date_of_value)
    
    # Test the as_float method
    result = money_instance.as_float()
    assert result == float(quantity), f"Expected {float(quantity)}, but got {result}"
