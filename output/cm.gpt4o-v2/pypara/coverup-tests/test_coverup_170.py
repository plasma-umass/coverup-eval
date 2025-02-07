# file: pypara/monetary.py:1384-1385
# asked: {"lines": [1384, 1385], "branches": []}
# gained: {"lines": [1384, 1385], "branches": []}

import pytest
from pypara.monetary import NonePrice
from pypara.currencies import Currency, CurrencyType

def test_noneprice_with_ccy():
    # Create a NonePrice instance
    none_price = NonePrice()
    
    # Create a Currency instance
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    
    # Call the with_ccy method
    result = none_price.with_ccy(currency)
    
    # Assert that the result is the same NonePrice instance
    assert result is none_price
