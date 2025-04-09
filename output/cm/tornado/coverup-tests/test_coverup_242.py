# file tornado/util.py:435-438
# lines [438]
# branches []

import datetime
import pytest

# Assuming the provided code snippet is part of the tornado.util module
from tornado.util import timedelta_to_seconds

def test_timedelta_to_seconds():
    # Create a timedelta object
    td = datetime.timedelta(days=1, seconds=30, microseconds=500000)
    
    # Calculate the expected result using the total_seconds method
    expected_seconds = td.total_seconds()
    
    # Call the function under test
    result_seconds = timedelta_to_seconds(td)
    
    # Assert that the result is as expected
    assert result_seconds == expected_seconds
