# file: pypara/monetary.py:548-550
# asked: {"lines": [548, 549, 550], "branches": []}
# gained: {"lines": [548, 549, 550], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_with_qty():
    # Setup initial SomeMoney instance
    currency = Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY)
    initial_qty = Decimal('100.00')
    date = Date(2023, 10, 1)
    some_money = SomeMoney(currency, initial_qty, date)
    
    # New quantity to set
    new_qty = Decimal('200.00')
    
    # Call the method
    new_some_money = some_money.with_qty(new_qty)
    
    # Assertions to verify the postconditions
    assert new_some_money.ccy == currency
    assert new_some_money.qty == new_qty.quantize(currency.quantizer)
    assert new_some_money.dov == date

    # Clean up (if necessary)
    del some_money
    del new_some_money

