# file: pypara/dcc.py:23-27
# asked: {"lines": [23, 27], "branches": []}
# gained: {"lines": [23, 27], "branches": []}

import pytest
from pypara.dcc import _as_ccys
from pypara.currencies import Currencies, Currency

def test_as_ccys():
    # Prepare a set of currency codes
    currency_codes = {'USD', 'EUR', 'JPY'}
    
    # Call the function
    result = _as_ccys(currency_codes)
    
    # Verify the result is a set of Currency objects
    assert all(isinstance(currency, Currency) for currency in result)
    
    # Verify the result contains the correct currencies
    expected_currencies = {Currencies['USD'], Currencies['EUR'], Currencies['JPY']}
    assert result == expected_currencies
