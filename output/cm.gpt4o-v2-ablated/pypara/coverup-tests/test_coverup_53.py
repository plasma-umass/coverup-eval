# file: pypara/exchange.py:16-31
# asked: {"lines": [26, 27, 28, 31], "branches": []}
# gained: {"lines": [26, 27, 28, 31], "branches": []}

import pytest
from pypara.exchange import FXRateLookupError
from datetime import date

class Currency:
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return self.code

@pytest.fixture
def mock_currency():
    return Currency("USD"), Currency("EUR")

@pytest.fixture
def mock_date():
    return date(2023, 1, 1)

def test_fx_rate_lookup_error_initialization(mock_currency, mock_date):
    ccy1, ccy2 = mock_currency
    asof = mock_date
    error = FXRateLookupError(ccy1, ccy2, asof)
    
    assert error.ccy1 == ccy1
    assert error.ccy2 == ccy2
    assert error.asof == asof
    assert str(error) == f"Foreign exchange rate for {ccy1}/{ccy2} not found as of {asof}"
