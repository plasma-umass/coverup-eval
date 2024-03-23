# file pypara/commons/zeitgeist.py:14-24
# lines [14, 15, 16, 21, 24]
# branches []

import datetime
from pypara.commons.zeitgeist import DateRange
import pytest

def test_date_range():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    date_range = DateRange(since=start_date, until=end_date)

    assert date_range.since == start_date
    assert date_range.until == end_date
