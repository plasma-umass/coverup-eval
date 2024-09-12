# file: pypara/dcc.py:715-754
# asked: {"lines": [715, 716, 739, 740, 742, 745, 746, 748, 751, 754], "branches": [[739, 740], [739, 742], [745, 746], [745, 748]]}
# gained: {"lines": [715, 716, 739, 740, 742, 745, 746, 748, 751, 754], "branches": [[739, 740], [739, 742], [745, 746], [745, 748]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.dcc import dcfc_30_360_german

def test_dcfc_30_360_german_case1():
    start = Date(2007, 12, 28)
    asof = Date(2008, 2, 28)
    end = asof
    result = round(dcfc_30_360_german(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16666666666667')

def test_dcfc_30_360_german_case2():
    start = Date(2007, 12, 28)
    asof = Date(2008, 2, 29)
    end = asof
    result = round(dcfc_30_360_german(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16944444444444')

def test_dcfc_30_360_german_case3():
    start = Date(2007, 10, 31)
    asof = Date(2008, 11, 30)
    end = asof
    result = round(dcfc_30_360_german(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.08333333333333')

def test_dcfc_30_360_german_case4():
    start = Date(2008, 2, 1)
    asof = Date(2009, 5, 31)
    end = asof
    result = round(dcfc_30_360_german(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.33055555555556')

def test_dcfc_30_360_german_start_last_day_of_month():
    start = Date(2007, 1, 31)
    asof = Date(2007, 2, 28)
    end = asof
    result = round(dcfc_30_360_german(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.07777777777778')

def test_dcfc_30_360_german_asof_last_day_of_month_not_end():
    start = Date(2007, 1, 30)
    asof = Date(2007, 2, 28)
    end = Date(2007, 3, 30)
    result = round(dcfc_30_360_german(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.08333333333333')
