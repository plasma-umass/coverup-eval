# file: tornado/util.py:435-438
# asked: {"lines": [435, 438], "branches": []}
# gained: {"lines": [435, 438], "branches": []}

import pytest
from datetime import timedelta
from tornado.util import timedelta_to_seconds

def test_timedelta_to_seconds():
    td = timedelta(days=1, seconds=1, microseconds=1)
    result = timedelta_to_seconds(td)
    expected = td.total_seconds()
    assert result == expected

    td_zero = timedelta(0)
    result_zero = timedelta_to_seconds(td_zero)
    expected_zero = td_zero.total_seconds()
    assert result_zero == expected_zero

    td_negative = timedelta(days=-1, seconds=-1, microseconds=-1)
    result_negative = timedelta_to_seconds(td_negative)
    expected_negative = td_negative.total_seconds()
    assert result_negative == expected_negative
