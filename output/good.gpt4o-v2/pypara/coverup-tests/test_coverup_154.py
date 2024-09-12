# file: pypara/monetary.py:695-696
# asked: {"lines": [695, 696], "branches": []}
# gained: {"lines": [695, 696], "branches": []}

import pytest
from pypara.monetary import NoneMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_none_money_convert():
    # Create a NoneMoney instance
    none_money = NoneMoney()

    # Create a Currency instance
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

    # Call the convert method
    result = none_money.convert(to=currency)

    # Assert that the result is the same instance
    assert result is none_money
