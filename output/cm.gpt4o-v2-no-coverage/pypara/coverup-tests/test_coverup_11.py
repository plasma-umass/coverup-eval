# file: pypara/dcc.py:220-237
# asked: {"lines": [220, 225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}
# gained: {"lines": [220, 225, 228, 229, 231, 234, 237], "branches": [[228, 229], [228, 231]]}

import datetime
from decimal import Decimal
from typing import Optional
import pytest
from unittest.mock import Mock
from pypara.commons.numbers import ZERO
from pypara.commons.zeitgeist import Date
from pypara.dcc import DCC

def test_calculate_daily_fraction():
    # Mock the calculate_fraction_method
    mock_calculate_fraction_method = Mock()
    mock_calculate_fraction_method.side_effect = [Decimal('0.1'), Decimal('0.2')]

    # Create a DCC instance with the mock method
    dcc = DCC(name="TestDCC", altnames=set(), currencies=set(), calculate_fraction_method=mock_calculate_fraction_method)

    # Define test dates
    start = Date(2023, 1, 1)
    asof = Date(2023, 1, 2)
    end = Date(2023, 12, 31)

    # Call the method
    result = dcc.calculate_daily_fraction(start, asof, end)

    # Assertions
    assert result == Decimal('0.1')
    mock_calculate_fraction_method.assert_any_call(start, asof - datetime.timedelta(days=1), end, None)
    mock_calculate_fraction_method.assert_any_call(start, asof, end, None)

def test_calculate_daily_fraction_asof_minus_1_less_than_start():
    # Mock the calculate_fraction_method
    mock_calculate_fraction_method = Mock()
    mock_calculate_fraction_method.return_value = Decimal('0.2')

    # Create a DCC instance with the mock method
    dcc = DCC(name="TestDCC", altnames=set(), currencies=set(), calculate_fraction_method=mock_calculate_fraction_method)

    # Define test dates
    start = Date(2023, 1, 2)
    asof = Date(2023, 1, 2)
    end = Date(2023, 12, 31)

    # Call the method
    result = dcc.calculate_daily_fraction(start, asof, end)

    # Assertions
    assert result == Decimal('0.2')
    mock_calculate_fraction_method.assert_called_once_with(start, asof, end, None)
