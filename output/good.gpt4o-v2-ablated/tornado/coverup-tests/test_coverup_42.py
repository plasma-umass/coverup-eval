# file: tornado/options.py:617-623
# asked: {"lines": [617, 618, 619, 620, 621, 622, 623], "branches": [[618, 619], [618, 623]]}
# gained: {"lines": [617], "branches": []}

import pytest
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

@pytest.fixture
def option():
    return _Option()

def test_parse_datetime_valid_date(option):
    result = option._parse_datetime("2023-10-01")
    assert result == datetime.datetime(2023, 10, 1)

def test_parse_datetime_valid_datetime(option):
    result = option._parse_datetime("2023-10-01 12:34:56")
    assert result == datetime.datetime(2023, 10, 1, 12, 34, 56)

def test_parse_datetime_invalid_format(option):
    with pytest.raises(Error, match="Unrecognized date/time format: 'invalid-date'"):
        option._parse_datetime("invalid-date")

def test_parse_datetime_partial_match(option):
    with pytest.raises(Error, match="Unrecognized date/time format: '2023-10-01 12:34'"):
        option._parse_datetime("2023-10-01 12:34")
