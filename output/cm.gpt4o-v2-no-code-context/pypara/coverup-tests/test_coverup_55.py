# file: pypara/monetary.py:1137-1139
# asked: {"lines": [1137, 1138, 1139], "branches": []}
# gained: {"lines": [1137, 1138, 1139], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

@pytest.fixture
def currency():
    return Currency("USD", "United States Dollar", 2, "fiat", Decimal("0.01"), None)

def test_someprice_round(currency):
    # Setup
    quantity = Decimal("123.456")
    dov = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, dov)
    
    # Execute
    rounded_price = some_price.round(2)
    
    # Verify
    assert rounded_price.ccy == currency
    assert rounded_price.qty == quantity.__round__(2)
    assert rounded_price.dov == dov

    # Cleanup is not necessary as no state is modified

def test_someprice_round_default(currency):
    # Setup
    quantity = Decimal("123.456")
    dov = Date(2023, 10, 1)
    some_price = SomePrice(currency, quantity, dov)
    
    # Execute
    rounded_price = some_price.round()
    
    # Verify
    assert rounded_price.ccy == currency
    assert rounded_price.qty == quantity.__round__(0)
    assert rounded_price.dov == dov

    # Cleanup is not necessary as no state is modified
