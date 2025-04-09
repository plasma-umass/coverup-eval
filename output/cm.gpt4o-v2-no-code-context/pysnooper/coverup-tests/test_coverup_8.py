# file: pysnooper/pycompat.py:90-97
# asked: {"lines": [90, 91, 92, 93, 95, 96, 97], "branches": []}
# gained: {"lines": [90, 91, 92, 93, 95, 96, 97], "branches": []}

import pytest
from datetime import timedelta as timedelta_module

# Assuming the function timedelta_parse is imported from pysnooper.pycompat
from pysnooper.pycompat import timedelta_parse

def test_timedelta_parse():
    # Test with a valid input string
    result = timedelta_parse("1:2:3.4")
    expected = timedelta_module(hours=1, minutes=2, seconds=3, microseconds=4)
    assert result == expected

    # Test with another valid input string
    result = timedelta_parse("10:20:30.400000")
    expected = timedelta_module(hours=10, minutes=20, seconds=30, microseconds=400000)
    assert result == expected

    # Test with edge case input string
    result = timedelta_parse("0:0:0.0")
    expected = timedelta_module(hours=0, minutes=0, seconds=0, microseconds=0)
    assert result == expected

    # Test with maximum values for each component
    result = timedelta_parse("23:59:59.999999")
    expected = timedelta_module(hours=23, minutes=59, seconds=59, microseconds=999999)
    assert result == expected

    # Test with minimum values for each component
    result = timedelta_parse("0:0:0.1")
    expected = timedelta_module(hours=0, minutes=0, seconds=0, microseconds=1)
    assert result == expected
