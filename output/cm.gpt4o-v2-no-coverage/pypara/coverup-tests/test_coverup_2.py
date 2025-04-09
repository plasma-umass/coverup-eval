# file: pypara/monetary.py:29-45
# asked: {"lines": [29, 30, 35, 40, 41, 42, 45], "branches": []}
# gained: {"lines": [29, 30, 35, 40, 41, 42, 45], "branches": []}

import pytest
from pypara.monetary import IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType

def test_incompatible_currency_error():
    # Create two different currencies
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    eur = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    
    # Create the error
    error = IncompatibleCurrencyError(usd, eur, "exchange")
    
    # Assertions to verify the error message and attributes
    assert error.ccy1 == usd
    assert error.ccy2 == eur
    assert error.operation == "exchange"
    assert str(error) == "USD vs EUR are incompatible for operation 'exchange'."
