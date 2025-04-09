# file: pypara/exchange.py:81-93
# asked: {"lines": [81, 93], "branches": []}
# gained: {"lines": [81, 93], "branches": []}

import pytest
from decimal import Decimal
from pypara.currencies import Currencies
from pypara.exchange import FXRate
import datetime

def test_fxrate_invert():
    # Arrange
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    date = datetime.date.today()
    value = Decimal("2")
    fx_rate = FXRate(ccy1, ccy2, date, value)
    
    # Act
    inverted_fx_rate = ~fx_rate
    
    # Assert
    assert inverted_fx_rate.ccy1 == ccy2
    assert inverted_fx_rate.ccy2 == ccy1
    assert inverted_fx_rate.date == date
    assert inverted_fx_rate.value == Decimal("0.5")
