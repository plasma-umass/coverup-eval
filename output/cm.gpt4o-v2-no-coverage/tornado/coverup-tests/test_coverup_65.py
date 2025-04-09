# file: tornado/options.py:617-623
# asked: {"lines": [617, 618, 619, 620, 621, 622, 623], "branches": [[618, 619], [618, 623]]}
# gained: {"lines": [617, 618, 619, 620, 621, 622, 623], "branches": [[618, 619], [618, 623]]}

import pytest
import datetime
from tornado.options import _Option, Error

class TestOption:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        self.option = _Option(name="test_option", default=None, type=str, help=None, metavar=None, multiple=False, file_name=None, group_name=None, callback=None)
        self.valid_date_str = "2023-10-01 12:00:00"
        self.invalid_date_str = "invalid-date"
        self.datetime_formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]
        monkeypatch.setattr(self.option, '_DATETIME_FORMATS', self.datetime_formats)

    def test_parse_datetime_valid(self):
        result = self.option._parse_datetime(self.valid_date_str)
        assert result == datetime.datetime.strptime(self.valid_date_str, "%Y-%m-%d %H:%M:%S")

    def test_parse_datetime_invalid(self):
        with pytest.raises(Error, match="Unrecognized date/time format: 'invalid-date'"):
            self.option._parse_datetime(self.invalid_date_str)
