# file: pypara/monetary.py:686-687
# asked: {"lines": [686, 687], "branches": []}
# gained: {"lines": [686, 687], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.currencies import Currency, CurrencyType

def test_none_money_with_ccy():
    # Create an instance of NoneMoney
    none_money = NoneMoney()

    # Create a dummy Currency instance using the Currency.of method
    dummy_currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

    # Call the with_ccy method
    result = none_money.with_ccy(dummy_currency)

    # Assert that the result is the same instance of NoneMoney
    assert result is none_money
