# file: pypara/monetary.py:441-443
# asked: {"lines": [442, 443], "branches": []}
# gained: {"lines": [442, 443], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_some_money_positive():
    # Arrange
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    quantity = Decimal("100.00")
    date_of_value = Date.today()
    some_money = SomeMoney(currency, quantity, date_of_value)
    
    # Act
    positive_money = some_money.positive()
    
    # Assert
    assert positive_money.ccy == currency
    assert positive_money.qty == quantity
    assert positive_money.dov == date_of_value
    assert isinstance(positive_money, SomeMoney)
