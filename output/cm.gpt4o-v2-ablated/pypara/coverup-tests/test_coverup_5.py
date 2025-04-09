# file: pypara/dcc.py:467-493
# asked: {"lines": [467, 468, 469, 470, 472, 493], "branches": []}
# gained: {"lines": [467, 468, 469, 470, 472, 493], "branches": []}

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_360

def test_dcfc_act_360_case1():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 28)
    end = asof
    result = round(dcfc_act_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.17222222222222')

def test_dcfc_act_360_case2():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 29)
    end = asof
    result = round(dcfc_act_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.17500000000000')

def test_dcfc_act_360_case3():
    start = date(2007, 10, 31)
    asof = date(2008, 11, 30)
    end = asof
    result = round(dcfc_act_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.10000000000000')

def test_dcfc_act_360_case4():
    start = date(2008, 2, 1)
    asof = date(2009, 5, 31)
    end = asof
    result = round(dcfc_act_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.34722222222222')
