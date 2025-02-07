# file: pypara/monetary.py:1393-1394
# asked: {"lines": [1393, 1394], "branches": []}
# gained: {"lines": [1393, 1394], "branches": []}

import pytest
from pypara.monetary import NonePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_none_price_convert():
    # Create a NonePrice instance
    none_price = NonePrice()

    # Create a Currency instance
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)

    # Call the convert method
    result = none_price.convert(to=currency)

    # Assert that the result is the same instance
    assert result is none_price
