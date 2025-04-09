# file: pypara/dcc.py:220-237
# asked: {"lines": [225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}
# gained: {"lines": [225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}

import pytest
from datetime import datetime, timedelta
from decimal import Decimal
from unittest.mock import MagicMock

# Assuming the DCC class and calculate_fraction_method are defined in pypara/dcc.py
from pypara.dcc import DCC

ZERO = Decimal('0')

@pytest.fixture
def dcc(mocker):
    calculate_fraction_method = mocker.Mock()
    return DCC(name='test', altnames=[], currencies=[], calculate_fraction_method=calculate_fraction_method)

def test_calculate_daily_fraction_asof_minus_1_before_start(dcc, mocker):
    start = datetime(2023, 1, 1)
    asof = datetime(2023, 1, 1)
    end = datetime(2023, 12, 31)
    freq = Decimal('1')

    dcc.calculate_fraction_method.return_value = Decimal('0.5')

    result = dcc.calculate_daily_fraction(start, asof, end, freq)
    
    assert result == Decimal('0.5')

def test_calculate_daily_fraction_asof_minus_1_after_start(dcc, mocker):
    start = datetime(2023, 1, 1)
    asof = datetime(2023, 1, 2)
    end = datetime(2023, 12, 31)
    freq = Decimal('1')

    dcc.calculate_fraction_method.side_effect = [Decimal('0.1'), Decimal('0.5')]

    result = dcc.calculate_daily_fraction(start, asof, end, freq)
    
    assert result == Decimal('0.4')
    dcc.calculate_fraction_method.assert_any_call(start, asof - timedelta(days=1), end, freq)
    dcc.calculate_fraction_method.assert_any_call(start, asof, end, freq)
