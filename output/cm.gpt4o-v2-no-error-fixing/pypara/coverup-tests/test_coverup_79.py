# file: pypara/monetary.py:29-45
# asked: {"lines": [40, 41, 42, 45], "branches": []}
# gained: {"lines": [40, 41, 42, 45], "branches": []}

import pytest
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import IncompatibleCurrencyError

def test_incompatible_currency_error():
    # Create two different currencies
    ccy1 = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    
    # Create the exception
    exception = IncompatibleCurrencyError(ccy1, ccy2, "addition")
    
    # Assertions to verify the exception's attributes
    assert exception.ccy1 == ccy1
    assert exception.ccy2 == ccy2
    assert exception.operation == "addition"
    assert str(exception) == "USD vs EUR are incompatible for operation 'addition'."

    # Test with default operation
    exception_default = IncompatibleCurrencyError(ccy1, ccy2)
    assert exception_default.operation == "<Unspecified>"
    assert str(exception_default) == "USD vs EUR are incompatible for operation '<Unspecified>'."
