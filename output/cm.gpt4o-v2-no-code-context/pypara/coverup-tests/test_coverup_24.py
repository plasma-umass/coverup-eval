# file: pypara/dcc.py:496-519
# asked: {"lines": [496, 497, 519], "branches": []}
# gained: {"lines": [496, 497, 519], "branches": []}

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_365_f

def test_dcfc_act_365_f_case1():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 28)
    end = asof
    result = dcfc_act_365_f(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.16986301369863')

def test_dcfc_act_365_f_case2():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 29)
    end = asof
    result = dcfc_act_365_f(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.17260273972603')

def test_dcfc_act_365_f_case3():
    start = date(2007, 10, 31)
    asof = date(2008, 11, 30)
    end = asof
    result = dcfc_act_365_f(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('1.08493150684932')

def test_dcfc_act_365_f_case4():
    start = date(2008, 2, 1)
    asof = date(2009, 5, 31)
    end = asof
    result = dcfc_act_365_f(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('1.32876712328767')
