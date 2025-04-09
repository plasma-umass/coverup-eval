# file: pypara/monetary.py:545-546
# asked: {"lines": [545, 546], "branches": []}
# gained: {"lines": [545, 546], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney

def test_some_money_with_ccy():
    # Setup initial SomeMoney instance
    original_currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    new_currency = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(original_currency, qty, dov)
    
    # Call with_ccy to get a new SomeMoney instance with a different currency
    new_some_money = some_money.with_ccy(new_currency)
    
    # Assertions to verify the correctness
    assert new_some_money.ccy == new_currency
    assert new_some_money.qty == qty
    assert new_some_money.dov == dov
    assert new_some_money != some_money  # Ensure it's a new instance

    # Clean up (not much to clean up in this case, but this is where you'd do it)

