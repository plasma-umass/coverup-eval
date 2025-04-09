# file: pypara/monetary.py:430-431
# asked: {"lines": [430, 431], "branches": []}
# gained: {"lines": [430, 431], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_some_money_as_integer():
    # Create a SomeMoney instance
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal('100.50')
    date_of_value = Date(2023, 10, 5)
    some_money = SomeMoney(ccy=currency, qty=quantity, dov=date_of_value)
    
    # Test as_integer method
    assert some_money.as_integer() == 100
