# file: pysnooper/pycompat.py:86-88
# asked: {"lines": [86, 87, 88], "branches": []}
# gained: {"lines": [86, 87, 88], "branches": []}

import pytest
import datetime as datetime_module
from pysnooper.pycompat import timedelta_format

def test_timedelta_format():
    # Test with a specific timedelta
    delta = datetime_module.timedelta(days=1, seconds=3600, microseconds=123456)
    result = timedelta_format(delta)
    expected_time = (datetime_module.datetime.min + delta).time().isoformat(timespec='microseconds')
    assert result == expected_time

    # Test with zero timedelta
    delta = datetime_module.timedelta(0)
    result = timedelta_format(delta)
    expected_time = (datetime_module.datetime.min + delta).time().isoformat(timespec='microseconds')
    assert result == expected_time

    # Test with a small negative timedelta that does not cause overflow
    delta = datetime_module.timedelta(microseconds=-1)
    with pytest.raises(OverflowError):
        timedelta_format(delta)

    # Test with a large negative timedelta that causes overflow
    delta = datetime_module.timedelta(days=-1)
    with pytest.raises(OverflowError):
        timedelta_format(delta)
