# file pypara/monetary.py:1119-1120
# lines [1119, 1120]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, Currency

@pytest.fixture
def currency_mock(mocker):
    Currency = mocker.Mock()
    Currency.return_value = Currency
    Currency.name = 'USD'
    Currency.decimals = 2
    Currency.type = 'fiat'
    Currency.quantizer = Decimal('0.01')
    Currency.hashcache = {}
    return Currency

def test_someprice_as_float(currency_mock):
    quantity = Decimal('123.45')
    date_of_value = Date(2023, 1, 1)
    some_price = SomePrice(ccy=currency_mock, qty=quantity, dov=date_of_value)
    
    result = some_price.as_float()
    
    assert result == 123.45, "The as_float method should return the correct float representation of the quantity"
