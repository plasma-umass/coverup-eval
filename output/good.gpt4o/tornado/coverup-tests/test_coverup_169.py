# file tornado/util.py:435-438
# lines [435, 438]
# branches []

import pytest
from datetime import timedelta
from tornado.util import timedelta_to_seconds

def test_timedelta_to_seconds():
    # Test with a positive timedelta
    td = timedelta(days=1, hours=2, minutes=3, seconds=4)
    assert timedelta_to_seconds(td) == 93784.0

    # Test with a zero timedelta
    td = timedelta()
    assert timedelta_to_seconds(td) == 0.0

    # Test with a negative timedelta
    td = timedelta(days=-1, hours=-2, minutes=-3, seconds=-4)
    assert timedelta_to_seconds(td) == -93784.0

    # Test with a fractional second
    td = timedelta(seconds=1.5)
    assert timedelta_to_seconds(td) == 1.5
