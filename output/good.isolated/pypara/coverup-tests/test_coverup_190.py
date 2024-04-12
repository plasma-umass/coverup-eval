# file pypara/monetary.py:552-553
# lines [552, 553]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Money, Date

@pytest.fixture
def currency():
    return Currency('USD', 'United States Dollar', 2, Decimal('0.01'), True, {})

@pytest.fixture
def quantity():
    return Decimal('100.00')

@pytest.fixture
def date_of_value():
    return Date(2023, 1, 1)

@pytest.fixture
def some_money(currency, quantity, date_of_value):
    return SomeMoney(currency, quantity, date_of_value)

def test_with_dov(some_money):
    new_dov = Date(2023, 1, 2)
    new_money = some_money.with_dov(new_dov)
    
    assert isinstance(new_money, Money), "The returned object should be an instance of Money"
    assert new_money.ccy == some_money.ccy, "The currency should remain unchanged"
    assert new_money.qty == some_money.qty, "The quantity should remain unchanged"
    assert new_money.dov == new_dov, "The date of value should be updated to the new value"
    assert new_money.dov != some_money.dov, "The date of value should be different from the original"
