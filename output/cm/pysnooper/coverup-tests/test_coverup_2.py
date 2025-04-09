# file pysnooper/pycompat.py:86-88
# lines [86, 87, 88]
# branches []

import datetime
import pytest
from pysnooper.pycompat import timedelta_format

def test_timedelta_format():
    # Create a timedelta object
    delta = datetime.timedelta(hours=2, minutes=30, seconds=15, microseconds=123456)
    
    # Call the function to test
    formatted_time = timedelta_format(delta)
    
    # Expected format: '02:30:15.123456'
    expected_format = '02:30:15.123456'
    
    # Assert the result is as expected
    assert formatted_time == expected_format
