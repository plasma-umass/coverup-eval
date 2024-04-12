# file pypara/dcc.py:149-173
# lines [160, 163, 166, 167, 168, 169, 170, 173]
# branches ['166->167', '166->173']

import datetime
from dateutil.relativedelta import relativedelta
import pytest

# Assuming the _next_payment_date function is part of a class or module named dcc
# If it's not, you would need to adjust the import below accordingly.
from pypara.dcc import _next_payment_date

def test_next_payment_date_eom_exception():
    # Test with a start date where replacing the day would cause an exception
    # For example, setting eom to 31 on a month with only 30 days
    start_date = datetime.date(2021, 4, 1)  # April has 30 days
    frequency = 1
    eom = 31

    # Expected result should be the next year's April date without changing the day to 31
    expected_date = datetime.date(2022, 4, 1)

    # Call the function with parameters that will trigger the exception block
    result = _next_payment_date(start_date, frequency, eom)

    # Assert that the result is as expected
    assert result == expected_date, "The _next_payment_date function should handle invalid eom by ignoring it."

# Note: No need for cleanup as the test does not modify any external state or configuration.
