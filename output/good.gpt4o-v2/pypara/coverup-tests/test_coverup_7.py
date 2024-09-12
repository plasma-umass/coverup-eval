# file: pypara/dcc.py:208-218
# asked: {"lines": [208, 213, 215, 218], "branches": [[213, 215], [213, 218]]}
# gained: {"lines": [208, 213, 215, 218], "branches": [[213, 215], [213, 218]]}

import pytest
from decimal import Decimal
from pypara.dcc import DCC
from pypara.commons.numbers import ZERO
from pypara.commons.zeitgeist import Date

def mock_methodology(start, asof, end, freq):
    return Decimal('0.5')

def test_calculate_fraction_invalid_dates():
    dcc = DCC(None, None, None, mock_methodology)
    start = Date(2023, 1, 1)
    asof = Date(2023, 1, 2)
    end = Date(2023, 1, 1)
    result = dcc.calculate_fraction(start, asof, end)
    assert result == ZERO

def test_calculate_fraction_valid_dates():
    dcc = DCC(None, None, None, mock_methodology)
    start = Date(2023, 1, 1)
    asof = Date(2023, 1, 2)
    end = Date(2023, 1, 3)
    result = dcc.calculate_fraction(start, asof, end)
    assert result == Decimal('0.5')
