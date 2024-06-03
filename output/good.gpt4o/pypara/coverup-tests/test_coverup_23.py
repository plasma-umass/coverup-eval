# file pypara/dcc.py:191-207
# lines [191, 192, 197, 200, 203, 206]
# branches []

import pytest
from pypara.dcc import DCC
from typing import NamedTuple, Set, Callable
import decimal
import datetime

# Mocking the Currency class for the test
class Currency(NamedTuple):
    code: str

# Mocking the DCFC type for the test
DCFC = Callable[[datetime.date, datetime.date, datetime.date, decimal.Decimal], decimal.Decimal]

def test_dcc_namedtuple():
    # Mocking a Currency and DCFC for the test
    mock_currency = Currency("USD")
    mock_calculate_fraction_method = lambda x, y, z, w: decimal.Decimal(0.5)
    
    # Creating an instance of DCC
    dcc_instance = DCC(
        name="Actual/360",
        altnames={"Act/360", "A/360"},
        currencies={mock_currency},
        calculate_fraction_method=mock_calculate_fraction_method
    )
    
    # Assertions to verify the DCC instance
    assert dcc_instance.name == "Actual/360"
    assert "Act/360" in dcc_instance.altnames
    assert mock_currency in dcc_instance.currencies
    assert dcc_instance.calculate_fraction_method == mock_calculate_fraction_method

    # Clean up if necessary (not needed in this case as no external state is modified)
