# file: pypara/dcc.py:600-635
# asked: {"lines": [600, 601, 624, 625, 628, 629, 632, 635], "branches": [[624, 625], [624, 628], [628, 629], [628, 632]]}
# gained: {"lines": [600, 601, 624, 625, 628, 629, 632, 635], "branches": [[624, 625], [624, 628], [628, 629], [628, 632]]}

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_30_360_isda

def test_dcfc_30_360_isda_case1():
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 28)
    end = asof
    result = round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16666666666667')

def test_dcfc_30_360_isda_case2():
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 29)
    end = asof
    result = round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16944444444444')

def test_dcfc_30_360_isda_case3():
    start = datetime.date(2007, 10, 31)
    asof = datetime.date(2008, 11, 30)
    end = asof
    result = round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.08333333333333')

def test_dcfc_30_360_isda_case4():
    start = datetime.date(2008, 2, 1)
    asof = datetime.date(2009, 5, 31)
    end = asof
    result = round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14)
    assert result == Decimal('1.33333333333333')

def test_dcfc_30_360_isda_start_day_31():
    start = datetime.date(2021, 1, 31)
    asof = datetime.date(2021, 2, 28)
    end = asof
    result = round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.07777777777778')

def test_dcfc_30_360_isda_asof_day_31():
    start = datetime.date(2021, 1, 30)
    asof = datetime.date(2021, 3, 31)
    end = asof
    result = round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14)
    assert result == Decimal('0.16666666666667')
