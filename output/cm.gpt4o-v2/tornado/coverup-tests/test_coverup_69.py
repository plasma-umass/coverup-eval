# file: tornado/options.py:617-623
# asked: {"lines": [617, 618, 619, 620, 621, 622, 623], "branches": [[618, 619], [618, 623]]}
# gained: {"lines": [617, 618, 619, 620, 621, 622, 623], "branches": [[618, 619], [618, 623]]}

import pytest
import datetime
from tornado.options import _Option, Error

class TestOption(_Option):
    _DATETIME_FORMATS = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"]

@pytest.fixture
def option():
    return TestOption(name="test", default=None, type=str, help=None, metavar=None, multiple=False, file_name=None, group_name=None, callback=None)

def test_parse_datetime_valid_format(option):
    assert option._parse_datetime("2023-10-01") == datetime.datetime(2023, 10, 1)
    assert option._parse_datetime("01-10-2023") == datetime.datetime(2023, 10, 1)

def test_parse_datetime_invalid_format(option):
    with pytest.raises(Error, match="Unrecognized date/time format: 'invalid-date'"):
        option._parse_datetime("invalid-date")
