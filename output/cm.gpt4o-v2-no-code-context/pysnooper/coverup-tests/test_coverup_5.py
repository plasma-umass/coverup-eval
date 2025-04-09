# file: pysnooper/pycompat.py:86-88
# asked: {"lines": [86, 87, 88], "branches": []}
# gained: {"lines": [86, 87, 88], "branches": []}

import pytest
from datetime import timedelta, datetime as datetime_module

# Assuming the function timedelta_format is defined in the module pysnooper.pycompat
from pysnooper.pycompat import timedelta_format

def test_timedelta_format():
    # Create a timedelta object
    delta = timedelta(days=1, seconds=3600, microseconds=123456)
    
    # Call the function
    result = timedelta_format(delta)
    
    # Calculate the expected result
    expected_time = (datetime_module.min + delta).time()
    expected_result = expected_time.isoformat(timespec='microseconds')
    
    # Assert the result is as expected
    assert result == expected_result
