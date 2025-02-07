# file: lib/ansible/module_utils/facts/system/date_time.py:27-68
# asked: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 52], [51, 54], [55, 56], [55, 57]]}
# gained: {"lines": [32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68], "branches": [[51, 54], [55, 57]]}

import pytest
import datetime
import time
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector

@pytest.fixture
def mock_time(monkeypatch):
    fixed_time = 1609459200  # Fixed timestamp for 2021-01-01 00:00:00 UTC

    class MockedDatetime(datetime.datetime):
        @classmethod
        def fromtimestamp(cls, ts, tz=None):
            return super().fromtimestamp(fixed_time, tz)

        @classmethod
        def utcfromtimestamp(cls, ts):
            return super().utcfromtimestamp(fixed_time)

    monkeypatch.setattr(time, 'time', lambda: fixed_time)
    monkeypatch.setattr(datetime, 'datetime', MockedDatetime)

def test_collect(mock_time):
    collector = DateTimeFactCollector()
    facts = collector.collect()

    assert 'date_time' in facts
    date_time_facts = facts['date_time']

    assert date_time_facts['year'] == '2021'
    assert date_time_facts['month'] == '01'
    assert date_time_facts['weekday'] == 'Friday'
    assert date_time_facts['weekday_number'] == '5'
    assert date_time_facts['weeknumber'] == '00'
    assert date_time_facts['day'] == '01'
    assert date_time_facts['hour'] == '00'
    assert date_time_facts['minute'] == '00'
    assert date_time_facts['second'] == '00'
    assert date_time_facts['epoch'] == '1609459200'
    assert date_time_facts['epoch_int'] == '1609459200'
    assert date_time_facts['date'] == '2021-01-01'
    assert date_time_facts['time'] == '00:00:00'
    assert date_time_facts['iso8601_micro'] == '2021-01-01T00:00:00.000000Z'
    assert date_time_facts['iso8601'] == '2021-01-01T00:00:00Z'
    assert date_time_facts['iso8601_basic'] == '20210101T000000000000'
    assert date_time_facts['iso8601_basic_short'] == '20210101T000000'
    assert date_time_facts['tz'] == time.strftime('%Z')
    assert date_time_facts['tz_dst'] == time.tzname[1]
    assert date_time_facts['tz_offset'] == time.strftime('%z')
