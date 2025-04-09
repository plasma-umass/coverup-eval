# file: pypara/dcc.py:208-218
# asked: {"lines": [208, 213, 215, 218], "branches": [[213, 215], [213, 218]]}
# gained: {"lines": [208, 213, 215, 218], "branches": [[213, 215], [213, 218]]}

import pytest
from decimal import Decimal
from pypara.commons.numbers import ZERO
from pypara.commons.zeitgeist import Date
from pypara.dcc import DCC

def test_calculate_fraction_valid_dates(monkeypatch):
    # Setup
    start = Date(2023, 1, 1)
    asof = Date(2023, 6, 1)
    end = Date(2023, 12, 31)
    freq = Decimal('1.0')
    
    def mock_calculate_fraction_method(start, asof, end, freq):
        return Decimal('0.5')
    
    dcc = DCC(name="TestDCC", altnames=set(), currencies=set(), calculate_fraction_method=mock_calculate_fraction_method)
    
    # Test
    result = dcc.calculate_fraction(start, asof, end, freq)
    
    # Assert
    assert result == Decimal('0.5')

def test_calculate_fraction_invalid_dates():
    # Setup
    start = Date(2023, 1, 1)
    asof = Date(2023, 6, 1)
    end = Date(2023, 5, 31)  # Invalid asof > end
    
    dcc = DCC(name="TestDCC", altnames=set(), currencies=set(), calculate_fraction_method=None)
    
    # Test
    result = dcc.calculate_fraction(start, asof, end)
    
    # Assert
    assert result == ZERO
