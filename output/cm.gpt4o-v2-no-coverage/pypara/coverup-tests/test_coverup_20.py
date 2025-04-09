# file: pypara/exchange.py:16-31
# asked: {"lines": [16, 17, 21, 26, 27, 28, 31], "branches": []}
# gained: {"lines": [16, 17, 21, 26, 27, 28, 31], "branches": []}

import pytest
from pypara.exchange import FXRateLookupError
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date
from decimal import Decimal

def test_fx_rate_lookup_error(mocker):
    # Mock the __str__ method of Currency to return the code
    mocker.patch.object(Currency, '__str__', lambda self: self.code)

    # Create instances of Currency and Date
    ccy1 = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    asof = Date(2023, 1, 1)

    # Create an instance of FXRateLookupError
    error = FXRateLookupError(ccy1, ccy2, asof)

    # Assertions to verify the state of the error
    assert error.ccy1 == ccy1
    assert error.ccy2 == ccy2
    assert error.asof == asof
    assert str(error) == "Foreign exchange rate for USD/EUR not found as of 2023-01-01"
