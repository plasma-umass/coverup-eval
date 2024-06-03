# file pypara/dcc.py:600-635
# lines [600, 601, 624, 625, 628, 629, 632, 635]
# branches ['624->625', '624->628', '628->629', '628->632']

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_30_360_isda

def test_dcfc_30_360_isda():
    # Test case where start day is 31
    start = datetime.date(2021, 1, 31)
    asof = datetime.date(2021, 2, 28)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.07777777777778')

    # Test case where start day is 30 and asof day is 31
    start = datetime.date(2021, 1, 30)
    asof = datetime.date(2021, 3, 31)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.16666666666667')

    # Test case where start day is not 31 and asof day is not 31
    start = datetime.date(2021, 1, 15)
    asof = datetime.date(2021, 2, 15)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.08333333333333')

    # Test case where start day is 31 and asof day is 31
    start = datetime.date(2021, 1, 31)
    asof = datetime.date(2021, 3, 31)
    end = asof
    result = dcfc_30_360_isda(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.16666666666667')
