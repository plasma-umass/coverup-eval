# file: pypara/dcc.py:548-571
# asked: {"lines": [571], "branches": []}
# gained: {"lines": [571], "branches": []}

import pytest
from datetime import date
from decimal import Decimal
import calendar
from pypara.dcc import dcfc_act_365_l

def test_dcfc_act_365_l_non_leap_year():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 28)
    end = asof
    result = dcfc_act_365_l(start=start, asof=asof, end=end)
    expected = Decimal('0.16939890710383')
    assert round(result, 14) == expected

def test_dcfc_act_365_l_leap_year():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 29)
    end = asof
    result = dcfc_act_365_l(start=start, asof=asof, end=end)
    expected = Decimal('0.17213114754098')
    assert round(result, 14) == expected

def test_dcfc_act_365_l_full_year_non_leap():
    start = date(2007, 10, 31)
    asof = date(2008, 11, 30)
    end = asof
    result = dcfc_act_365_l(start=start, asof=asof, end=end)
    expected = Decimal('1.08196721311475')
    assert round(result, 14) == expected

def test_dcfc_act_365_l_full_year_leap():
    start = date(2008, 2, 1)
    asof = date(2009, 5, 31)
    end = asof
    result = dcfc_act_365_l(start=start, asof=asof, end=end)
    expected = Decimal('1.32876712328767')
    assert round(result, 14) == expected
