# file: pypara/dcc.py:208-218
# asked: {"lines": [208, 213, 215, 218], "branches": [[213, 215], [213, 218]]}
# gained: {"lines": [208, 213, 215, 218], "branches": [[213, 215], [213, 218]]}

import pytest
from decimal import Decimal
from pypara.dcc import DCC
from pypara.commons.numbers import ZERO
from pypara.commons.zeitgeist import Date

def test_calculate_fraction_invalid_dates():
    dcc = DCC(name="test", altnames=set(), currencies=set(), calculate_fraction_method=lambda start, asof, end, freq: Decimal('1.0'))
    start = Date(2023, 1, 1)
    asof = Date(2023, 1, 2)
    end = Date(2023, 1, 1)
    
    result = dcc.calculate_fraction(start, asof, end)
    
    assert result == ZERO

def test_calculate_fraction_valid_dates():
    dcc = DCC(name="test", altnames=set(), currencies=set(), calculate_fraction_method=lambda start, asof, end, freq: Decimal('1.0'))
    start = Date(2023, 1, 1)
    asof = Date(2023, 1, 2)
    end = Date(2023, 1, 3)
    
    result = dcc.calculate_fraction(start, asof, end)
    
    assert result == Decimal('1.0')
