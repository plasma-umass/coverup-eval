# file pypara/dcc.py:86-146
# lines [86, 121, 124, 127, 130, 133, 136, 139, 142, 143, 146]
# branches ['142->143', '142->146']

import datetime
from decimal import Decimal
from typing import Union, Optional
import pytest
from pypara.dcc import _last_payment_date

def _construct_date(year: int, month: int, day: int) -> datetime.date:
    """
    Helper function to construct a date safely.
    """
    try:
        return datetime.date(year, month, day)
    except ValueError:
        # Handle cases where the day is out of range for the month
        if month == 2 and day == 29:
            return datetime.date(year, 2, 28)
        elif day > 30 and month in [4, 6, 9, 11]:
            return datetime.date(year, month, 30)
        else:
            raise

@pytest.mark.parametrize("start, asof, frequency, eom, expected", [
    (datetime.date(2014, 1, 1), datetime.date(2015, 12, 31), 1, None, datetime.date(2015, 1, 1)),
    (datetime.date(2015, 1, 1), datetime.date(2015, 12, 31), 1, None, datetime.date(2015, 1, 1)),
    (datetime.date(2014, 1, 1), datetime.date(2015, 12, 31), 2, None, datetime.date(2015, 7, 1)),
    (datetime.date(2014, 1, 1), datetime.date(2015, 8, 31), 2, None, datetime.date(2015, 7, 1)),
    (datetime.date(2014, 1, 1), datetime.date(2015, 4, 30), 2, None, datetime.date(2015, 1, 1)),
    (datetime.date(2014, 6, 1), datetime.date(2015, 4, 30), 1, None, datetime.date(2014, 6, 1)),
    (datetime.date(2008, 7, 7), datetime.date(2015, 10, 6), 4, None, datetime.date(2015, 7, 7)),
    (datetime.date(2014, 12, 9), datetime.date(2015, 12, 4), 1, None, datetime.date(2014, 12, 9)),
    (datetime.date(2012, 12, 15), datetime.date(2016, 1, 6), 2, None, datetime.date(2015, 12, 15)),
    (datetime.date(2012, 12, 15), datetime.date(2015, 12, 31), 2, None, datetime.date(2015, 12, 15)),
    (datetime.date(2014, 1, 1), datetime.date(2015, 12, 31), 1, 31, datetime.date(2015, 1, 31)),
    (datetime.date(2014, 1, 1), datetime.date(2015, 12, 31), 2, 15, datetime.date(2015, 7, 15)),
])
def test_last_payment_date(start, asof, frequency, eom, expected):
    result = _last_payment_date(start, asof, frequency, eom)
    assert result == expected
