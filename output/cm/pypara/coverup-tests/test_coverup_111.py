# file pypara/dcc.py:86-146
# lines [86, 121, 124, 127, 130, 133, 136, 139, 142, 143, 146]
# branches ['142->143', '142->146']

import datetime
import pytest
from pypara.dcc import _last_payment_date

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_last_payment_date_edge_cases(cleanup):
    # Test with a start date that is a leap day
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2017, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2016, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2018, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2017, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 29)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 29)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 29)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 29)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 29)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 29)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2020, 2, 29)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is after leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 3, 1)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2020, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2019, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is before leap day in a non-leap year
    start_date = datetime.date(2016, 2, 29)
    asof_date = datetime.date(2019, 2, 28)
    frequency = 1
    eom = None
    expected_date = datetime.date(2018, 2, 28)
    assert _last_payment_date(start_date, asof_date, frequency, eom) == expected_date

    # Test with a start date that is a leap day and asof date is leap day in a leap year
    start_date = datetime.date(2016, 2, 29)
