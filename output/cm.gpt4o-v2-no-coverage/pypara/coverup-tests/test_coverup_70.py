# file: pypara/monetary.py:468-471
# asked: {"lines": [468, 470, 471], "branches": []}
# gained: {"lines": [468, 470, 471], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_scalar_add():
    # Setup
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    money = SomeMoney(currency, quantity, date)
    
    # Test addition with integer
    result = money.scalar_add(10)
    assert result.qty == Decimal('110.00')
    assert result.ccy == currency
    assert result.dov == date
    
    # Test addition with float
    result = money.scalar_add(10.5)
    assert result.qty == Decimal('110.50')
    assert result.ccy == currency
    assert result.dov == date
    
    # Test addition with Decimal
    result = money.scalar_add(Decimal('10.25'))
    assert result.qty == Decimal('110.25')
    assert result.ccy == currency
    assert result.dov == date

    # Test addition with string
    result = money.scalar_add('10.75')
    assert result.qty == Decimal('110.75')
    assert result.ccy == currency
    assert result.dov == date
