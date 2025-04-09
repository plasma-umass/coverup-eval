# file: pypara/dcc.py:676-712
# asked: {"lines": [676, 677, 701, 702, 705, 706, 709, 712], "branches": [[701, 702], [701, 705], [705, 706], [705, 709]]}
# gained: {"lines": [676, 677, 701, 702, 705, 706, 709, 712], "branches": [[701, 702], [701, 705], [705, 706], [705, 709]]}

import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_30_e_plus_360

def test_dcfc_30_e_plus_360_case1():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 28)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16666666666667')

def test_dcfc_30_e_plus_360_case2():
    start = date(2007, 12, 28)
    asof = date(2008, 2, 29)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16944444444444')

def test_dcfc_30_e_plus_360_case3():
    start = date(2007, 10, 31)
    asof = date(2008, 11, 30)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.08333333333333')

def test_dcfc_30_e_plus_360_case4():
    start = date(2008, 2, 1)
    asof = date(2009, 5, 31)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.33333333333333')

def test_dcfc_30_e_plus_360_start_day_31():
    start = date(2007, 12, 31)
    asof = date(2008, 2, 28)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16111111111111')

def test_dcfc_30_e_plus_360_asof_day_31():
    start = date(2007, 12, 28)
    asof = date(2008, 1, 31)
    end = asof
    result = round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.09166666666667')
