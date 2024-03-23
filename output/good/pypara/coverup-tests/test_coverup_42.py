# file pypara/dcc.py:574-597
# lines [574, 575, 597]
# branches []

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_nl_365
from datetime import date

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Teardown if necessary

def test_dcfc_nl_365_with_leap_day(cleanup):
    start = date(2007, 12, 28)
    asof_with_leap = date(2008, 2, 29)
    end_with_leap = date(2008, 2, 29)
    expected_result_with_leap = Decimal('0.16986301369863')
    result_with_leap = round(dcfc_nl_365(start=start, asof=asof_with_leap, end=end_with_leap), 14)
    assert result_with_leap == expected_result_with_leap

def test_dcfc_nl_365_without_leap_day(cleanup):
    start = date(2007, 12, 28)
    asof_without_leap = date(2008, 2, 28)
    end_without_leap = date(2008, 2, 28)
    expected_result_without_leap = Decimal('0.16986301369863')
    result_without_leap = round(dcfc_nl_365(start=start, asof=asof_without_leap, end=end_without_leap), 14)
    assert result_without_leap == expected_result_without_leap
