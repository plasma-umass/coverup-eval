# file: pysnooper/pycompat.py:90-97
# asked: {"lines": [90, 91, 92, 93, 95, 96, 97], "branches": []}
# gained: {"lines": [90, 91, 92, 93, 95, 96, 97], "branches": []}

import pytest
import datetime as datetime_module
from pysnooper.pycompat import timedelta_parse

def test_timedelta_parse():
    # Test normal case
    result = timedelta_parse("1:2:3.4")
    expected = datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=4)
    assert result == expected

    # Test edge case with zero values
    result = timedelta_parse("0:0:0.0")
    expected = datetime_module.timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
    assert result == expected

    # Test case with maximum values for hours, minutes, seconds, and microseconds
    result = timedelta_parse("23:59:59.999999")
    expected = datetime_module.timedelta(hours=23, minutes=59, seconds=59, microseconds=999999)
    assert result == expected

    # Test case with invalid format
    with pytest.raises(ValueError):
        timedelta_parse("invalid:format:string")

    # Test case with missing microseconds
    with pytest.raises(ValueError):
        timedelta_parse("1:2:3")

    # Test case with missing seconds and microseconds
    with pytest.raises(ValueError):
        timedelta_parse("1:2")

    # Test case with missing minutes, seconds, and microseconds
    with pytest.raises(ValueError):
        timedelta_parse("1")
