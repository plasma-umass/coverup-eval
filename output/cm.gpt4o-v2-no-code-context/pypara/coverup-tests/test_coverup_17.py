# file: pypara/dcc.py:638-673
# asked: {"lines": [638, 639, 662, 663, 666, 667, 670, 673], "branches": [[662, 663], [662, 666], [666, 667], [666, 670]]}
# gained: {"lines": [638, 639, 662, 663, 666, 667, 670, 673], "branches": [[662, 663], [662, 666], [666, 667], [666, 670]]}

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import dcfc_30_e_360

def test_dcfc_30_e_360_start_day_31():
    start = datetime.date(2021, 1, 31)
    asof = datetime.date(2021, 2, 28)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    expected = Decimal('0.07777777777778')
    assert round(result, 14) == expected

def test_dcfc_30_e_360_asof_day_31():
    start = datetime.date(2021, 1, 30)
    asof = datetime.date(2021, 3, 31)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    expected = Decimal('0.16666666666667')
    assert round(result, 14) == expected

def test_dcfc_30_e_360_both_days_31():
    start = datetime.date(2021, 1, 31)
    asof = datetime.date(2021, 3, 31)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    expected = Decimal('0.16666666666667')
    assert round(result, 14) == expected

def test_dcfc_30_e_360_no_31_days():
    start = datetime.date(2021, 1, 30)
    asof = datetime.date(2021, 2, 28)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    expected = Decimal('0.07777777777778')
    assert round(result, 14) == expected
