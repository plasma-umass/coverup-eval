# file: pypara/dcc.py:600-635
# asked: {"lines": [600, 601, 624, 625, 628, 629, 632, 635], "branches": [[624, 625], [624, 628], [628, 629], [628, 632]]}
# gained: {"lines": [600, 601, 624, 625, 628, 629, 632, 635], "branches": [[624, 625], [624, 628], [628, 629], [628, 632]]}

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import dcfc_30_360_isda

def test_dcfc_30_360_isda_start_day_31():
    start = datetime.date(2023, 1, 31)
    asof = datetime.date(2023, 2, 28)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    expected = Decimal('0.07777777777778')
    assert round(result, 14) == expected

def test_dcfc_30_360_isda_asof_day_31():
    start = datetime.date(2023, 1, 30)
    asof = datetime.date(2023, 3, 31)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    expected = Decimal('0.16666666666667')
    assert round(result, 14) == expected

def test_dcfc_30_360_isda_start_day_30_asof_day_31():
    start = datetime.date(2023, 1, 30)
    asof = datetime.date(2023, 3, 31)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    expected = Decimal('0.16666666666667')
    assert round(result, 14) == expected

def test_dcfc_30_360_isda_normal_case():
    start = datetime.date(2023, 1, 15)
    asof = datetime.date(2023, 2, 15)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    expected = Decimal('0.08333333333333')
    assert round(result, 14) == expected
