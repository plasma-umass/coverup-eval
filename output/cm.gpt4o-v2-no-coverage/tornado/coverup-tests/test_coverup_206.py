# file: tornado/options.py:643-658
# asked: {"lines": [644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658], "branches": [[647, 648], [647, 656], [649, 650], [649, 651]]}
# gained: {"lines": [644, 645, 646, 647, 648, 649, 651, 652, 653, 654, 655, 656, 657, 658], "branches": [[647, 648], [647, 656], [649, 651]]}

import pytest
import datetime
from tornado.options import _Option

class TestOption:
    def test_parse_timedelta(self, monkeypatch):
        option = _Option(name="test", type=str)

        # Test valid timedelta string
        monkeypatch.setattr(option, '_TIMEDELTA_PATTERN', _Option._TIMEDELTA_PATTERN)
        monkeypatch.setattr(option, '_TIMEDELTA_ABBREV_DICT', _Option._TIMEDELTA_ABBREV_DICT)
        result = option._parse_timedelta("1h 30m")
        assert result == datetime.timedelta(hours=1, minutes=30)

        # Test invalid timedelta string
        with pytest.raises(Exception):
            option._parse_timedelta("1x 30m")
