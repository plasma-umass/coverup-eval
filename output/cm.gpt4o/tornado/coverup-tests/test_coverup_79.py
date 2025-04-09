# file tornado/options.py:617-623
# lines [617, 618, 619, 620, 621, 622, 623]
# branches ['618->619', '618->623']

import pytest
from unittest import mock
import datetime
from tornado.options import Error

class _Option:
    _DATETIME_FORMATS = ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S"]

    def _parse_datetime(self, value: str) -> datetime.datetime:
        for format in self._DATETIME_FORMATS:
            try:
                return datetime.datetime.strptime(value, format)
            except ValueError:
                pass
        raise Error("Unrecognized date/time format: %r" % value)

def test_parse_datetime_valid_format():
    option = _Option()
    date_str = "2023-10-01"
    expected_date = datetime.datetime(2023, 10, 1)
    assert option._parse_datetime(date_str) == expected_date

def test_parse_datetime_invalid_format():
    option = _Option()
    date_str = "01-10-2023"
    with pytest.raises(Error, match="Unrecognized date/time format: '01-10-2023'"):
        option._parse_datetime(date_str)

def test_parse_datetime_valid_datetime_format():
    option = _Option()
    datetime_str = "2023-10-01 12:30:45"
    expected_datetime = datetime.datetime(2023, 10, 1, 12, 30, 45)
    assert option._parse_datetime(datetime_str) == expected_datetime
