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
    currency = Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY)
    quantity = Decimal('100.00')
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Test scalar_add with a numeric value
    result = some_money.scalar_add(50)
    
    # Assertions
    assert result.ccy == currency
    assert result.qty == Decimal('150.00').quantize(currency.quantizer)
    assert result.dov == date_of_value

    # Test scalar_add with a Decimal value
    result = some_money.scalar_add(Decimal('25.50'))
    
    # Assertions
    assert result.ccy == currency
    assert result.qty == Decimal('125.50').quantize(currency.quantizer)
    assert result.dov == date_of_value

    # Test scalar_add with a float value
    result = some_money.scalar_add(25.75)
    
    # Assertions
    assert result.ccy == currency
    assert result.qty == Decimal('125.75').quantize(currency.quantizer)
    assert result.dov == date_of_value
