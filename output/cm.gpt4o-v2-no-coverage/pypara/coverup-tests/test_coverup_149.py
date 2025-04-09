# file: pypara/monetary.py:1240-1241
# asked: {"lines": [1240, 1241], "branches": []}
# gained: {"lines": [1240, 1241], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

def test_someprice_with_ccy():
    # Setup initial SomePrice instance
    original_ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    new_ccy = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    price = SomePrice(original_ccy, qty, dov)
    
    # Call with_ccy to get a new SomePrice instance with a different currency
    new_price = price.with_ccy(new_ccy)
    
    # Assertions to verify the correctness of the new SomePrice instance
    assert new_price.ccy == new_ccy
    assert new_price.qty == qty
    assert new_price.dov == dov
    assert new_price != price  # Ensure it's a new instance

    # Clean up (if necessary)
    del price
    del new_price
