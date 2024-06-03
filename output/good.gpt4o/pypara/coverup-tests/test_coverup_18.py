# file pypara/dcc.py:638-673
# lines [638, 639, 662, 663, 666, 667, 670, 673]
# branches ['662->663', '662->666', '666->667', '666->670']

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_30_e_360

def test_dcfc_30_e_360():
    # Test case where start day is 31
    start = datetime.date(2021, 1, 31)
    asof = datetime.date(2021, 2, 28)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.07777777777778')

    # Test case where asof day is 31
    start = datetime.date(2021, 1, 30)
    asof = datetime.date(2021, 3, 31)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.16666666666667')

    # Test case where both start and asof days are 31
    start = datetime.date(2021, 1, 31)
    asof = datetime.date(2021, 3, 31)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.16666666666667')

    # Test case where neither start nor asof days are 31
    start = datetime.date(2021, 1, 30)
    asof = datetime.date(2021, 2, 28)
    end = asof
    result = dcfc_30_e_360(start=start, asof=asof, end=end)
    assert round(result, 14) == Decimal('0.07777777777778')
