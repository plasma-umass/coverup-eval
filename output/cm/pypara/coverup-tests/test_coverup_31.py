# file pypara/dcc.py:399-440
# lines [399, 400, 424, 427, 430, 432, 434, 437, 440]
# branches ['430->432', '430->440', '432->434', '432->437']

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_act_act
from datetime import date

def test_dcfc_act_act_leap_and_non_leap_years():
    # Test with a range that includes both leap and non-leap years
    start = date(2019, 12, 31)  # Non-leap year
    asof = date(2021, 1, 1)     # Includes leap year 2020
    end = asof
    result = dcfc_act_act(start=start, asof=asof, end=end)
    expected_days_non_leap = (date(2020, 1, 1) - start).days
    expected_days_leap = (asof - date(2020, 1, 1)).days
    expected = Decimal(expected_days_non_leap) / Decimal(365) + Decimal(expected_days_leap) / Decimal(366)
    assert result == expected, "Day count fraction for period including leap and non-leap years is incorrect"
