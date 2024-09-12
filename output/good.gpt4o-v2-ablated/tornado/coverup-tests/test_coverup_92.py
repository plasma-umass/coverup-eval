# file: tornado/util.py:435-438
# asked: {"lines": [435, 438], "branches": []}
# gained: {"lines": [435, 438], "branches": []}

import pytest
from datetime import timedelta
from tornado.util import timedelta_to_seconds

def test_timedelta_to_seconds_positive():
    td = timedelta(days=1, hours=2, minutes=3, seconds=4)
    result = timedelta_to_seconds(td)
    assert result == 93784.0

def test_timedelta_to_seconds_zero():
    td = timedelta(0)
    result = timedelta_to_seconds(td)
    assert result == 0.0

def test_timedelta_to_seconds_negative():
    td = timedelta(days=-1, hours=-2, minutes=-3, seconds=-4)
    result = timedelta_to_seconds(td)
    assert result == -93784.0
