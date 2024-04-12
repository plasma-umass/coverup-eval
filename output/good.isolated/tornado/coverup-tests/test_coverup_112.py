# file tornado/options.py:617-623
# lines [617, 618, 619, 620, 621, 622, 623]
# branches ['618->619', '618->623']

import datetime
import pytest
from tornado.options import Error, _Option

# Assuming the _Option class has a _DATETIME_FORMATS attribute
# which is a list of datetime formats to try parsing the value with.
# Also assuming that the _Option class requires a 'name' and 'type' argument in its constructor.

@pytest.fixture
def option_with_datetime_formats():
    option = _Option(name='test_option', type=str)
    option._DATETIME_FORMATS = ['%Y-%m-%d', '%H:%M:%S']
    return option

def test_parse_valid_datetime(option_with_datetime_formats):
    valid_date_str = '2023-01-01'
    expected_date = datetime.datetime.strptime(valid_date_str, '%Y-%m-%d')
    assert option_with_datetime_formats._parse_datetime(valid_date_str) == expected_date

    valid_time_str = '23:59:59'
    expected_time = datetime.datetime.strptime(valid_time_str, '%H:%M:%S')
    assert option_with_datetime_formats._parse_datetime(valid_time_str) == expected_time

def test_parse_invalid_datetime(option_with_datetime_formats):
    invalid_datetime_str = 'not-a-date'
    with pytest.raises(Error) as exc_info:
        option_with_datetime_formats._parse_datetime(invalid_datetime_str)
    assert "Unrecognized date/time format" in str(exc_info.value)
