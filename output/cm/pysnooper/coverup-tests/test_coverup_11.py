# file pysnooper/pycompat.py:90-97
# lines [90, 91, 92, 93, 95, 96, 97]
# branches []

import pytest
from datetime import timedelta
from pysnooper.pycompat import timedelta_parse

def test_timedelta_parse():
    # Test with a string that includes hours, minutes, seconds, and microseconds
    input_str = "2:30:15:123456"
    expected_timedelta = timedelta(hours=2, minutes=30, seconds=15, microseconds=123456)
    result = timedelta_parse(input_str)
    assert result == expected_timedelta, "The timedelta object does not match the expected value"

    # Test with a string that includes hours, minutes, seconds, and zero microseconds
    input_str = "1:22:33:0"
    expected_timedelta = timedelta(hours=1, minutes=22, seconds=33, microseconds=0)
    result = timedelta_parse(input_str)
    assert result == expected_timedelta, "The timedelta object does not match the expected value"

    # Test with a string that includes hours, minutes, seconds, and microseconds with dot
    input_str = "0:45:10.500000"
    expected_timedelta = timedelta(hours=0, minutes=45, seconds=10, microseconds=500000)
    result = timedelta_parse(input_str)
    assert result == expected_timedelta, "The timedelta object does not match the expected value"

    # Test with a string that includes hours, minutes, seconds, and microseconds without dot
    input_str = "3:25:45:789000"
    expected_timedelta = timedelta(hours=3, minutes=25, seconds=45, microseconds=789000)
    result = timedelta_parse(input_str)
    assert result == expected_timedelta, "The timedelta object does not match the expected value"
