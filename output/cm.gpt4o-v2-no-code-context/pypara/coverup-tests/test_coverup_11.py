# file: pypara/exchange.py:16-31
# asked: {"lines": [16, 17, 21, 26, 27, 28, 31], "branches": []}
# gained: {"lines": [16, 17, 21, 26, 27, 28, 31], "branches": []}

import pytest

# Mock classes to replace the missing imports
class Currency:
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return self.code

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

from pypara.exchange import FXRateLookupError

def test_fx_rate_lookup_error_initialization():
    ccy1 = Currency("USD")
    ccy2 = Currency("EUR")
    asof = Date(2023, 10, 1)
    
    error = FXRateLookupError(ccy1, ccy2, asof)
    
    assert error.ccy1 == ccy1
    assert error.ccy2 == ccy2
    assert error.asof == asof
    assert str(error) == "Foreign exchange rate for USD/EUR not found as of 2023-10-01"
