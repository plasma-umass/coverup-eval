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
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    money = SomeMoney(currency, quantity, date)
    
    # New quantity to set
    new_quantity = Decimal('200.00')
    
    # Call with_qty method
    new_money = money.with_qty(new_quantity)
    
    # Assertions to verify the postconditions
    assert new_money.qty == new_quantity.quantize(currency.quantizer)
    assert new_money.ccy == currency
    assert new_money.dov == date
