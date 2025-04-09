# file pypara/exchange.py:81-93
# lines [81, 93]
# branches []

import pytest
from decimal import Decimal
import datetime
from pypara.currencies import Currencies
from pypara.exchange import FXRate

def test_fxrate_inversion():
    # Arrange
    eur = Currencies["EUR"]
    usd = Currencies["USD"]
    today = datetime.date.today()
    rate_value = Decimal("2")
    inverted_rate_value = Decimal("0.5")
    
    nrate = FXRate(eur, usd, today, rate_value)
    expected_rrate = FXRate(usd, eur, today, inverted_rate_value)
    
    # Act
    rrate = ~nrate
    
    # Assert
    assert rrate == expected_rrate
