# file: pypara/dcc.py:757-805
# asked: {"lines": [757, 758, 781, 782, 785, 787, 790, 791, 794, 795, 798, 799, 802, 805], "branches": [[785, 787], [785, 794], [790, 791], [790, 794], [794, 795], [794, 798], [798, 799], [798, 802]]}
# gained: {"lines": [757, 758, 781, 782, 785, 787, 790, 791, 794, 795, 798, 802, 805], "branches": [[785, 787], [785, 794], [790, 791], [790, 794], [794, 795], [794, 798], [798, 802]]}

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import dcfc_30_360_us

def test_dcfc_30_360_us_case1():
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 28)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16666666666667')

def test_dcfc_30_360_us_case2():
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 29)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16944444444444')

def test_dcfc_30_360_us_case3():
    start = datetime.date(2007, 10, 31)
    asof = datetime.date(2008, 11, 30)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.08333333333333')

def test_dcfc_30_360_us_case4():
    start = datetime.date(2008, 2, 1)
    asof = datetime.date(2009, 5, 31)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.33333333333333')

def test_dcfc_30_360_us_last_day_of_month_start():
    start = datetime.date(2007, 12, 31)
    asof = datetime.date(2008, 1, 30)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.08333333333333')

def test_dcfc_30_360_us_last_day_of_month_asof():
    start = datetime.date(2007, 12, 30)
    asof = datetime.date(2008, 1, 31)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.08333333333333')

def test_dcfc_30_360_us_both_last_day_of_month():
    start = datetime.date(2007, 12, 31)
    asof = datetime.date(2008, 1, 31)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.08333333333333')

def test_dcfc_30_360_us_d2_is_31():
    start = datetime.date(2007, 12, 30)
    asof = datetime.date(2008, 1, 31)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.08333333333333')

def test_dcfc_30_360_us_d1_is_31():
    start = datetime.date(2007, 12, 31)
    asof = datetime.date(2008, 1, 30)
    end = asof
    result = round(dcfc_30_360_us(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.08333333333333')
