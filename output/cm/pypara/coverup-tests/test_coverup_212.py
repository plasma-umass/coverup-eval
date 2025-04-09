# file pypara/dcc.py:600-635
# lines [624, 625, 628, 629, 632, 635]
# branches ['624->625', '624->628', '628->629', '628->632']

import pytest
import datetime
from decimal import Decimal
from pypara.dcc import dcfc_30_360_isda

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup if necessary
    yield
    # No cleanup actions required for this test

def test_dcfc_30_360_isda_coverage(cleanup):
    # Test to cover lines 624-635 in dcfc_30_360_isda function
    start_date = datetime.date(2021, 3, 31)  # start.day == 31
    asof_date = datetime.date(2021, 5, 31)   # asof.day == 31 and start.day == 30 after adjustment
    end_date = asof_date

    # Expected behavior: start.day should be adjusted to 30, asof.day should be adjusted to 30
    # The number of days (nod) should be calculated correctly and the day count fraction returned
    expected_day_count_fraction = Decimal((30 - 30) + 30 * (5 - 3) + 360 * (2021 - 2021)) / Decimal(360)
    result = dcfc_30_360_isda(start=start_date, asof=asof_date, end=end_date)

    assert result == expected_day_count_fraction, "Day count fraction does not match expected value."

    # Ensure that the start and asof dates are adjusted correctly
    assert start_date.day == 31, "Start date day should not be modified."
    assert asof_date.day == 31, "Asof date day should not be modified."
