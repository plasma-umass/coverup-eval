# file pypara/monetary.py:427-428
# lines [427, 428]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Date

@pytest.fixture
def currency():
    return Currency('USD', 'US Dollar', 2, 'currency', {}, True)

def test_some_money_as_float(currency):
    quantity = Decimal('123.45')
    date_of_value = Date(2023, 1, 1)
    some_money = SomeMoney(ccy=currency, qty=quantity, dov=date_of_value)
    
    result = some_money.as_float()
    
    assert result == 123.45, "The as_float method should return the correct float representation of the quantity"
