# file: pypara/exchange.py:16-31
# asked: {"lines": [16, 17, 21, 26, 27, 28, 31], "branches": []}
# gained: {"lines": [16, 17, 21, 26, 27, 28, 31], "branches": []}

import pytest
from pypara.exchange import FXRateLookupError
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_fx_rate_lookup_error():
    # Arrange
    ccy1 = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    asof = Date.today()

    # Act
    error = FXRateLookupError(ccy1, ccy2, asof)

    # Assert
    assert error.ccy1 == ccy1
    assert error.ccy2 == ccy2
    assert error.asof == asof
    assert str(error) == f"Foreign exchange rate for {ccy1}/{ccy2} not found as of {asof}"
