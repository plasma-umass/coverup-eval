# file pypara/dcc.py:638-673
# lines [662, 663, 666, 667, 670, 673]
# branches ['662->663', '662->666', '666->667', '666->670']

import pytest
import datetime
from decimal import Decimal
from pypara.dcc import dcfc_30_e_360

def test_dcfc_30_e_360_coverage():
    # Test to cover lines 662-673 in dcfc_30_e_360 function
    start_date_with_31 = datetime.date(2007, 12, 31)
    asof_date_with_31 = datetime.date(2008, 1, 31)
    end_date = asof_date_with_31  # end date is the same as asof date for simplicity

    # Call the function with a start date and asof date that have day 31
    result = dcfc_30_e_360(start=start_date_with_31, asof=asof_date_with_31, end=end_date)

    # Assert that the start and asof dates are adjusted to day 30
    # and the correct day count fraction is returned
    expected_nod = (30 - 30) + 30 * (1 - 12) + 360 * (2008 - 2007)
    expected_result = Decimal(expected_nod) / Decimal(360)
    assert result == expected_result
