# file: pypara/monetary.py:1243-1244
# asked: {"lines": [1243, 1244], "branches": []}
# gained: {"lines": [1243, 1244], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price, Currency, SomePrice

def test_someprice_with_qty():
    # Setup initial SomePrice instance
    initial_qty = Decimal('100.00')
    new_qty = Decimal('200.00')
    ccy = Currency('USD', 'United States Dollar', 2, 'fiat', Decimal('0.01'), None)
    dov = Date(2023, 1, 1)
    some_price = SomePrice(ccy, initial_qty, dov)
    
    # Call with_qty to create a new SomePrice instance with updated quantity
    new_some_price = some_price.with_qty(new_qty)
    
    # Assertions to verify the new SomePrice instance
    assert new_some_price.ccy == ccy
    assert new_some_price.qty == new_qty
    assert new_some_price.dov == dov
    assert new_some_price != some_price  # Ensure it's a new instance

    # Clean up (not strictly necessary here, but good practice)
    del some_price
    del new_some_price
