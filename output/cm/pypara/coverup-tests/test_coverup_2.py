# file pypara/exchange.py:16-31
# lines [16, 17, 21, 26, 27, 28, 31]
# branches []

import pytest
from pypara.exchange import FXRateLookupError
from datetime import date

class Currency:
    pass

@pytest.fixture
def currency_pair():
    ccy1 = Currency()
    ccy2 = Currency()
    return ccy1, ccy2

def test_fx_rate_lookup_error(currency_pair):
    ccy1, ccy2 = currency_pair
    asof_date = date.today()
    with pytest.raises(FXRateLookupError) as exc_info:
        raise FXRateLookupError(ccy1, ccy2, asof_date)
    assert str(exc_info.value) == f"Foreign exchange rate for {ccy1}/{ccy2} not found as of {asof_date}"
    assert exc_info.value.ccy1 is ccy1
    assert exc_info.value.ccy2 is ccy2
    assert exc_info.value.asof == asof_date
