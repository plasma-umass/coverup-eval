# file: pysnooper/pycompat.py:86-88
# asked: {"lines": [86, 87, 88], "branches": []}
# gained: {"lines": [86, 87, 88], "branches": []}

import pytest
import datetime as datetime_module
from pysnooper.pycompat import timedelta_format

def test_timedelta_format():
    # Create a timedelta object
    delta = datetime_module.timedelta(seconds=1, microseconds=123456)
    
    # Call the function
    result = timedelta_format(delta)
    
    # Assert the result is as expected
    assert result == "00:00:01.123456"

    # Clean up (not much to clean up in this case, but this is a placeholder)
    del delta
    del result
