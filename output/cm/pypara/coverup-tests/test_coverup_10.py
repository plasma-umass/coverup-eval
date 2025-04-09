# file pypara/monetary.py:29-45
# lines [29, 30, 35, 40, 41, 42, 45]
# branches []

import pytest
from pypara.monetary import IncompatibleCurrencyError, Currency

class MockCurrency:
    def __init__(self, code):
        self.code = code

def test_incompatible_currency_error():
    # Mocking Currency class with a 'code' attribute
    ccy1 = MockCurrency('USD')
    ccy2 = MockCurrency('EUR')
    operation = 'addition'

    # Create the IncompatibleCurrencyError instance
    error = IncompatibleCurrencyError(ccy1, ccy2, operation)

    # Assertions to verify postconditions
    assert error.ccy1 == ccy1
    assert error.ccy2 == ccy2
    assert error.operation == operation
    assert str(error) == "USD vs EUR are incompatible for operation 'addition'."
