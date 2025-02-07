# file: pypara/monetary.py:1119-1120
# asked: {"lines": [1119, 1120], "branches": []}
# gained: {"lines": [1119, 1120], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_someprice_as_float():
    # Arrange
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    quantity = Decimal("123.45")
    date_of_value = Date.today()
    some_price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)

    # Act
    result = some_price.as_float()

    # Assert
    assert result == float(quantity)
