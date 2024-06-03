# file pypara/dcc.py:715-754
# lines [739, 740, 742, 745, 746, 748, 751, 754]
# branches ['739->740', '739->742', '745->746', '745->748']

import pytest
from datetime import date, timedelta
from decimal import Decimal
from pypara.dcc import dcfc_30_360_german

def _is_last_day_of_month(dt):
    next_day = dt + timedelta(days=1)
    return next_day.month != dt.month

@pytest.mark.parametrize("start, asof, end, expected", [
    (date(2007, 12, 31), date(2008, 2, 28), date(2008, 2, 28), Decimal('0.16111111111111')),
    (date(2007, 12, 31), date(2008, 2, 29), date(2008, 2, 29), Decimal('0.16388888888889')),
    (date(2007, 10, 31), date(2008, 11, 30), date(2008, 11, 30), Decimal('1.08333333333333')),
    (date(2008, 2, 1), date(2009, 5, 31), date(2009, 5, 31), Decimal('1.33055555555556')),
])
def test_dcfc_30_360_german(start, asof, end, expected):
    result = dcfc_30_360_german(start=start, asof=asof, end=end)
    assert round(result, 14) == expected
