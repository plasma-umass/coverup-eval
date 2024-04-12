# file pypara/dcc.py:23-27
# lines [23, 27]
# branches []

import pytest
from pypara.dcc import _as_ccys
from pypara.currencies import Currencies, Currency

def test_as_ccys():
    # Setup: Define a set of currency codes
    currency_codes = {'USD', 'EUR'}
    
    # Exercise: Convert currency codes to currencies
    result = _as_ccys(currency_codes)
    
    # Verify: Check if the result is a set of Currency objects
    assert isinstance(result, set)
    assert all(isinstance(c, Currency) for c in result)
    assert Currencies['USD'] in result
    assert Currencies['EUR'] in result
    
    # Cleanup: No cleanup required as no external state was modified
