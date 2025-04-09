# file: pypara/exchange.py:81-93
# asked: {"lines": [81, 93], "branches": []}
# gained: {"lines": [81, 93], "branches": []}

import pytest
from decimal import Decimal
import datetime
from pypara.currencies import Currencies
from pypara.exchange import FXRate

def test_fxrate_invert():
    # Arrange
    eur = Currencies["EUR"]
    usd = Currencies["USD"]
    today = datetime.date.today()
    rate_value = Decimal("2")
    inverted_rate_value = Decimal("0.5")
    
    fx_rate = FXRate(eur, usd, today, rate_value)
    expected_inverted_fx_rate = FXRate(usd, eur, today, inverted_rate_value)
    
    # Act
    inverted_fx_rate = ~fx_rate
    
    # Assert
    assert inverted_fx_rate == expected_inverted_fx_rate
