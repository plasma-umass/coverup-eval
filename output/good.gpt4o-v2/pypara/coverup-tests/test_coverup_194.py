# file: pypara/monetary.py:424-425
# asked: {"lines": [425], "branches": []}
# gained: {"lines": [425], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_as_boolean():
    # Create a mock currency
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    
    # Create a SomeMoney instance with a non-zero quantity
    some_money = SomeMoney(ccy=currency, qty=Decimal('10.00'), dov=Date.today())
    
    # Assert that as_boolean returns True for non-zero quantity
    assert some_money.as_boolean() is True
    
    # Create a SomeMoney instance with a zero quantity
    some_money_zero = SomeMoney(ccy=currency, qty=Decimal('0.00'), dov=Date.today())
    
    # Assert that as_boolean returns False for zero quantity
    assert some_money_zero.as_boolean() is False
