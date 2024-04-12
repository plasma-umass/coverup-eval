# file pypara/dcc.py:496-519
# lines [496, 497, 519]
# branches []

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_act_365_f
from datetime import date

def test_dcfc_act_365_f():
    start_date = date(2020, 1, 1)
    asof_date = date(2020, 6, 1)
    end_date = date(2020, 6, 1)
    expected_dcf = Decimal('0.41643835616438')  # (152 days) / 365
    result = dcfc_act_365_f(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == expected_dcf
