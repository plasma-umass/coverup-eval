# file: pypara/monetary.py:29-45
# asked: {"lines": [29, 30, 35, 40, 41, 42, 45], "branches": []}
# gained: {"lines": [29, 30, 35, 40, 41, 42, 45], "branches": []}

import pytest
from pypara.monetary import IncompatibleCurrencyError, Currency

def test_incompatible_currency_error_initialization():
    ccy1 = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=None, hashcache=None)
    ccy2 = Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=None, hashcache=None)
    operation = "addition"
    
    error = IncompatibleCurrencyError(ccy1, ccy2, operation)
    
    assert error.ccy1 == ccy1
    assert error.ccy2 == ccy2
    assert error.operation == operation
    assert str(error) == "USD vs EUR are incompatible for operation 'addition'."

def test_incompatible_currency_error_default_operation():
    ccy1 = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=None, hashcache=None)
    ccy2 = Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=None, hashcache=None)
    
    error = IncompatibleCurrencyError(ccy1, ccy2)
    
    assert error.ccy1 == ccy1
    assert error.ccy2 == ccy2
    assert error.operation == "<Unspecified>"
    assert str(error) == "USD vs EUR are incompatible for operation '<Unspecified>'."
