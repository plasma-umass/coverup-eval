# file: pypara/monetary.py:496-499
# asked: {"lines": [498, 499], "branches": []}
# gained: {"lines": [498, 499], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_some_money_multiply():
    # Setup
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date)
    
    # Test multiplication with an integer
    result = some_money.multiply(2)
    assert result.qty == Decimal('200.00')
    assert result.ccy == currency
    assert result.dov == date
    
    # Test multiplication with a float
    result = some_money.multiply(2.5)
    assert result.qty == Decimal('250.00')
    assert result.ccy == currency
    assert result.dov == date
    
    # Test multiplication with a Decimal
    result = some_money.multiply(Decimal('1.5'))
    assert result.qty == Decimal('150.00')
    assert result.ccy == currency
    assert result.dov == date
    
    # Test multiplication with a string
    result = some_money.multiply('3')
    assert result.qty == Decimal('300.00')
    assert result.ccy == currency
    assert result.dov == date
