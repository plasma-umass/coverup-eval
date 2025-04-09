# file: tornado/util.py:435-438
# asked: {"lines": [435, 438], "branches": []}
# gained: {"lines": [435, 438], "branches": []}

import pytest
from datetime import timedelta

# Import the function to be tested
from tornado.util import timedelta_to_seconds

def test_timedelta_to_seconds():
    # Test with a positive timedelta
    td = timedelta(days=1, hours=2, minutes=3, seconds=4)
    result = timedelta_to_seconds(td)
    assert result == 93784.0  # 1 day + 2 hours + 3 minutes + 4 seconds in total seconds

    # Test with a zero timedelta
    td = timedelta()
    result = timedelta_to_seconds(td)
    assert result == 0.0

    # Test with a negative timedelta
    td = timedelta(days=-1, hours=-2, minutes=-3, seconds=-4)
    result = timedelta_to_seconds(td)
    assert result == -93784.0  # -1 day - 2 hours - 3 minutes - 4 seconds in total seconds
