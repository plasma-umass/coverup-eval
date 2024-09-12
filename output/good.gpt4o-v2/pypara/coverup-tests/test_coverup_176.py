# file: pypara/monetary.py:1116-1117
# asked: {"lines": [1116, 1117], "branches": []}
# gained: {"lines": [1116, 1117], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_someprice_as_boolean():
    # Arrange
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    quantity = Decimal("100.00")
    date_of_value = Date.today()
    some_price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)

    # Act
    result = some_price.as_boolean()

    # Assert
    assert result is True

    # Clean up
    del some_price, currency, quantity, date_of_value

def test_someprice_as_boolean_zero_qty():
    # Arrange
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    quantity = Decimal("0.00")
    date_of_value = Date.today()
    some_price = SomePrice(ccy=currency, qty=quantity, dov=date_of_value)

    # Act
    result = some_price.as_boolean()

    # Assert
    assert result is False

    # Clean up
    del some_price, currency, quantity, date_of_value
