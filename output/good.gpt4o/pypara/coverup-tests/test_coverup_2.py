# file pypara/exchange.py:34-80
# lines [34, 35, 70, 73, 76, 79]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.currencies import Currencies
from pypara.exchange import FXRate

def test_fxrate_creation():
    # Create an FXRate instance
    rate = FXRate(Currencies["EUR"], Currencies["USD"], date.today(), Decimal("2"))
    
    # Unpack the FXRate instance
    ccy1, ccy2, rate_date, value = rate
    
    # Assertions to verify the FXRate instance
    assert ccy1 == Currencies["EUR"]
    assert ccy2 == Currencies["USD"]
    assert rate_date == date.today()
    assert value == Decimal("2")
