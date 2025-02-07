# file: pypara/dcc.py:23-27
# asked: {"lines": [23, 27], "branches": []}
# gained: {"lines": [23, 27], "branches": []}

import pytest
from pypara.dcc import _as_ccys
from pypara.currencies import Currencies, Currency, CurrencyLookupError

def test_as_ccys():
    # Test with a valid set of currency codes
    codes = {'USD', 'EUR'}
    expected = {Currencies['USD'], Currencies['EUR']}
    result = _as_ccys(codes)
    assert result == expected

    # Test with an empty set of currency codes
    codes = set()
    expected = set()
    result = _as_ccys(codes)
    assert result == expected

    # Test with an invalid currency code
    with pytest.raises(CurrencyLookupError):
        _as_ccys({'INVALID_CODE'})
