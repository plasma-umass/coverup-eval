# file pypara/exchange.py:95-127
# lines [95, 96, 109, 110, 111, 112, 113, 114, 115, 116, 119, 120, 123, 124, 127]
# branches ['109->110', '109->111', '111->112', '111->113', '113->114', '113->115', '115->116', '115->119', '119->120', '119->123', '123->124', '123->127']

import pytest
from decimal import Decimal
from datetime import date
from pypara.currencies import Currency, Currencies
from pypara.exchange import FXRate

def test_fxrate_of_valid():
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    fx_date = date.today()
    value = Decimal("2")
    
    fx_rate = FXRate.of(ccy1, ccy2, fx_date, value)
    
    assert fx_rate.ccy1 == ccy1
    assert fx_rate.ccy2 == ccy2
    assert fx_rate.date == fx_date
    assert fx_rate.value == value

def test_fxrate_of_invalid_currency1():
    ccy1 = "EUR"  # Invalid type
    ccy2 = Currencies["USD"]
    fx_date = date.today()
    value = Decimal("2")
    
    with pytest.raises(ValueError, match="CCY/1 must be of type `Currency`."):
        FXRate.of(ccy1, ccy2, fx_date, value)

def test_fxrate_of_invalid_currency2():
    ccy1 = Currencies["EUR"]
    ccy2 = "USD"  # Invalid type
    fx_date = date.today()
    value = Decimal("2")
    
    with pytest.raises(ValueError, match="CCY/2 must be of type `Currency`."):
        FXRate.of(ccy1, ccy2, fx_date, value)

def test_fxrate_of_invalid_value():
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    fx_date = date.today()
    value = Decimal("-1")  # Invalid value
    
    with pytest.raises(ValueError, match="FX rate value can not be equal to or less than `zero`."):
        FXRate.of(ccy1, ccy2, fx_date, value)

def test_fxrate_of_invalid_same_currency_value():
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["EUR"]
    fx_date = date.today()
    value = Decimal("2")  # Invalid value for same currency
    
    with pytest.raises(ValueError, match="FX rate to the same currency must be `one`."):
        FXRate.of(ccy1, ccy2, fx_date, value)
