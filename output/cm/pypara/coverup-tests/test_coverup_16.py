# file pypara/dcc.py:30-39
# lines [30, 38, 39]
# branches ['38->exit', '38->39']

import datetime
import pytest
from pypara.dcc import _get_date_range

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_get_date_range(cleanup):
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 1, 5)
    expected_dates = [
        datetime.date(2023, 1, 1),
        datetime.date(2023, 1, 2),
        datetime.date(2023, 1, 3),
        datetime.date(2023, 1, 4)
    ]
    result_dates = list(_get_date_range(start_date, end_date))
    assert result_dates == expected_dates, "The generated date range does not match the expected range"
