# file: pypara/commons/zeitgeist.py:14-24
# asked: {"lines": [14, 15, 16, 21, 24], "branches": []}
# gained: {"lines": [14, 15, 16, 21, 24], "branches": []}

import pytest
import datetime
from dataclasses import FrozenInstanceError
from pypara.commons.zeitgeist import DateRange

def test_daterange_initialization():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    date_range = DateRange(since=start_date, until=end_date)
    
    assert date_range.since == start_date
    assert date_range.until == end_date

def test_daterange_immutable():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    date_range = DateRange(since=start_date, until=end_date)
    
    with pytest.raises(FrozenInstanceError):
        date_range.since = datetime.date(2022, 1, 1)
    
    with pytest.raises(FrozenInstanceError):
        date_range.until = datetime.date(2022, 12, 31)
