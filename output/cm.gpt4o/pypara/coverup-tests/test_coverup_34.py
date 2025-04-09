# file pypara/dcc.py:149-173
# lines [149, 160, 163, 166, 167, 168, 169, 170, 173]
# branches ['166->167', '166->173']

import datetime
from decimal import Decimal
from dateutil.relativedelta import relativedelta
import pytest
from pypara.dcc import _next_payment_date

def test_next_payment_date():
    # Test case 1: No end of month specified
    start_date = datetime.date(2014, 1, 1)
    frequency = 1
    expected_date = datetime.date(2015, 1, 1)
    assert _next_payment_date(start_date, frequency) == expected_date

    # Test case 2: End of month specified
    start_date = datetime.date(2014, 1, 1)
    frequency = 1
    eom = 15
    expected_date = datetime.date(2015, 1, 15)
    assert _next_payment_date(start_date, frequency, eom) == expected_date

    # Test case 3: End of month specified but invalid day (e.g., February 30)
    start_date = datetime.date(2014, 1, 1)
    frequency = 1
    eom = 30
    expected_date = datetime.date(2015, 1, 30)  # Should fall back to the last valid day of the month
    assert _next_payment_date(start_date, frequency, eom) == expected_date

    # Test case 4: Frequency as Decimal
    start_date = datetime.date(2014, 1, 1)
    frequency = Decimal('1')
    expected_date = datetime.date(2015, 1, 1)
    assert _next_payment_date(start_date, frequency) == expected_date

    # Test case 5: Frequency as Decimal with end of month
    start_date = datetime.date(2014, 1, 1)
    frequency = Decimal('1')
    eom = 15
    expected_date = datetime.date(2015, 1, 15)
    assert _next_payment_date(start_date, frequency, eom) == expected_date

    # Test case 6: Frequency as Decimal with invalid end of month
    start_date = datetime.date(2014, 1, 1)
    frequency = Decimal('1')
    eom = 30
    expected_date = datetime.date(2015, 1, 30)  # Should fall back to the last valid day of the month
    assert _next_payment_date(start_date, frequency, eom) == expected_date
