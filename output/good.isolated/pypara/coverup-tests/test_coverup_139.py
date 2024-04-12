# file pypara/dcc.py:42-55
# lines [42, 55]
# branches []

import datetime
import pytest
from pypara.dcc import _get_actual_day_count

def test_get_actual_day_count():
    start_date = datetime.date(2020, 1, 1)
    end_date_same = datetime.date(2020, 1, 1)
    end_date_next_day = datetime.date(2020, 1, 2)
    end_date_next_month = datetime.date(2020, 2, 1)
    
    # Test for same day
    assert _get_actual_day_count(start_date, end_date_same) == 0
    
    # Test for next day
    assert _get_actual_day_count(start_date, end_date_next_day) == 1
    
    # Test for next month
    assert _get_actual_day_count(start_date, end_date_next_month) == 31
