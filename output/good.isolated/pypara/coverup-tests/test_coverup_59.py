# file pypara/dcc.py:548-571
# lines [548, 549, 571]
# branches []

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_act_365_l
from datetime import date

def test_dcfc_act_365_l_non_leap_year():
    start_date = date(2019, 1, 1)
    asof_date = date(2019, 12, 31)
    end_date = asof_date
    expected_dcf = Decimal('0.99726027397260')  # 365 days in a non-leap year
    result = dcfc_act_365_l(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == expected_dcf

def test_dcfc_act_365_l_leap_year():
    start_date = date(2020, 1, 1)
    asof_date = date(2020, 12, 31)
    end_date = asof_date
    expected_dcf = Decimal('0.99726775956284')  # 366 days in a leap year
    result = dcfc_act_365_l(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == expected_dcf
