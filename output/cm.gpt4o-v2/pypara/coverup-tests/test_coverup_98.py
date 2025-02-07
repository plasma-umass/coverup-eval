# file: pypara/monetary.py:1187-1190
# asked: {"lines": [1187, 1189, 1190], "branches": []}
# gained: {"lines": [1187, 1189, 1190], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_someprice_multiply():
    # Setup
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("100.00")
    date = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, date)
    
    # Test multiplication with an integer
    result = some_price.multiply(2)
    assert result.qty == quantity * Decimal(2)
    assert result.ccy == currency
    assert result.dov == date
    
    # Test multiplication with a float
    result = some_price.multiply(2.5)
    assert result.qty == quantity * Decimal(2.5)
    assert result.ccy == currency
    assert result.dov == date
    
    # Test multiplication with a Decimal
    result = some_price.multiply(Decimal("3.5"))
    assert result.qty == quantity * Decimal("3.5")
    assert result.ccy == currency
    assert result.dov == date
    
    # Test multiplication with a string that can be converted to Decimal
    result = some_price.multiply("4.5")
    assert result.qty == quantity * Decimal("4.5")
    assert result.ccy == currency
    assert result.dov == date
