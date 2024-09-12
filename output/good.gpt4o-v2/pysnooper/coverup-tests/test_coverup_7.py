# file: pysnooper/pycompat.py:86-88
# asked: {"lines": [86, 87, 88], "branches": []}
# gained: {"lines": [86, 87, 88], "branches": []}

import pytest
import datetime
from pysnooper.pycompat import timedelta_format

def test_timedelta_format():
    # Create a timedelta object
    delta = datetime.timedelta(seconds=1, microseconds=123456)
    
    # Call the function
    result = timedelta_format(delta)
    
    # Assert the result is as expected
    assert result == "00:00:01.123456"

