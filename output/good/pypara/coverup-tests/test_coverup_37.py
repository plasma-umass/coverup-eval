# file pypara/dcc.py:715-754
# lines [715, 716, 739, 740, 742, 745, 746, 748, 751, 754]
# branches ['739->740', '739->742', '745->746', '745->748']

import pytest
from decimal import Decimal
from pypara.dcc import dcfc_30_360_german
from datetime import date, timedelta

def _is_last_day_of_month(dt):
    """
    Helper function to determine if the date is the last day of the month.
    """
    next_month = dt.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day) == dt

@pytest.fixture
def mock_is_last_day_of_month(mocker):
    """
    Pytest fixture to mock the _is_last_day_of_month function.
    """
    return mocker.patch('pypara.dcc._is_last_day_of_month', side_effect=_is_last_day_of_month)

def test_dcfc_30_360_german_end_not_asof(mock_is_last_day_of_month):
    # Test case where asof is the last day of February in a leap year, but end is not asof
    start_date = date(2008, 2, 29)
    asof_date = date(2008, 2, 29)
    end_date = date(2008, 3, 1)  # end is not asof
    result = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    expected_result = Decimal('0') / Decimal('360')
    assert result == expected_result

    # Test case where asof is the last day of February in a non-leap year, but end is not asof
    start_date = date(2007, 2, 28)
    asof_date = date(2007, 2, 28)
    end_date = date(2007, 3, 1)  # end is not asof
    result = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    expected_result = Decimal('0') / Decimal('360')
    assert result == expected_result

    # Test case where asof is not the last day of the month and end is not asof
    start_date = date(2007, 2, 27)
    asof_date = date(2007, 2, 27)
    end_date = date(2007, 3, 1)  # end is not asof
    result = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    expected_result = Decimal('0') / Decimal('360')
    assert result == expected_result

    # Test case where asof is the 31st of a month and end is not asof
    start_date = date(2007, 1, 31)
    asof_date = date(2007, 1, 31)
    end_date = date(2007, 2, 1)  # end is not asof
    result = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    expected_result = Decimal('0') / Decimal('360')
    assert result == expected_result

    # Clean up after the test
    mock_is_last_day_of_month.stop()
