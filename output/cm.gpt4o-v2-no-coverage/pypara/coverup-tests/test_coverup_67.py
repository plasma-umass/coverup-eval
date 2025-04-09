# file: pypara/monetary.py:441-443
# asked: {"lines": [441, 442, 443], "branches": []}
# gained: {"lines": [441, 442, 443], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

def test_some_money_positive(usd_currency):
    # Arrange
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(usd_currency, quantity, date_of_value)
    
    # Act
    positive_money = some_money.positive()
    
    # Assert
    assert positive_money.ccy == usd_currency
    assert positive_money.qty == quantity
    assert positive_money.dov == date_of_value

def test_some_money_pos_operator(usd_currency):
    # Arrange
    quantity = Decimal("100.00")
    date_of_value = Date(2023, 10, 1)
    some_money = SomeMoney(usd_currency, quantity, date_of_value)
    
    # Act
    positive_money = +some_money
    
    # Assert
    assert positive_money.ccy == usd_currency
    assert positive_money.qty == quantity
    assert positive_money.dov == date_of_value
