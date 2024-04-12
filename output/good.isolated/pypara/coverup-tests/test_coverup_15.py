# file pypara/exchange.py:34-80
# lines [34, 35, 70, 73, 76, 79]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.exchange import FXRate
from pypara.currencies import Currencies

@pytest.fixture
def fx_rate():
    return FXRate(Currencies["EUR"], Currencies["USD"], date.today(), Decimal("1.5"))

def test_fx_rate_namedtuple_access(fx_rate):
    assert fx_rate.ccy1 == Currencies["EUR"], "The first currency should be EUR"
    assert fx_rate.ccy2 == Currencies["USD"], "The second currency should be USD"
    assert fx_rate.date == date.today(), "The date should be today's date"
    assert fx_rate.value == Decimal("1.5"), "The value should be 1.5"

    # Testing indexed access to properties
    assert fx_rate[0] == Currencies["EUR"], "Indexed access to ccy1 should return EUR"
    assert fx_rate[1] == Currencies["USD"], "Indexed access to ccy2 should return USD"
    assert fx_rate[2] == date.today(), "Indexed access to date should return today's date"
    assert fx_rate[3] == Decimal("1.5"), "Indexed access to value should return 1.5"
