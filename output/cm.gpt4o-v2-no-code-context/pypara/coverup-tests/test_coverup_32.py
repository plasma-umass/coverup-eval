# file: pypara/dcc.py:522-545
# asked: {"lines": [522, 523, 545], "branches": []}
# gained: {"lines": [522, 523, 545], "branches": []}

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_365_a

def test_dcfc_act_365_a_non_leap_year():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 28)
    end = asof
    result = dcfc_act_365_a(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.16986301369863')

def test_dcfc_act_365_a_leap_year():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 29)
    end = asof
    result = dcfc_act_365_a(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.17213114754098')

def test_dcfc_act_365_a_full_year():
    start = date(2007, 10, 31)
    asof = date(2008, 11, 30)
    end = asof
    result = dcfc_act_365_a(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('1.08196721311475')

def test_dcfc_act_365_a_more_than_year():
    start = date(2008, 2, 1)
    asof = date(2009, 5, 31)
    end = asof
    result = dcfc_act_365_a(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('1.32513661202186')
