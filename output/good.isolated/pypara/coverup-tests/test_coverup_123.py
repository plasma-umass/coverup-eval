# file pypara/exchange.py:81-93
# lines [81, 93]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.exchange import FXRate
from pypara.currencies import Currencies

@pytest.fixture
def fx_rate():
    return FXRate(Currencies["EUR"], Currencies["USD"], date.today(), Decimal("2"))

def test_invert_fx_rate(fx_rate):
    inverted_rate = ~fx_rate
    assert inverted_rate[0] == fx_rate[1]
    assert inverted_rate[1] == fx_rate[0]
    assert inverted_rate[2] == fx_rate[2]
    assert inverted_rate[3] == Decimal("0.5")
