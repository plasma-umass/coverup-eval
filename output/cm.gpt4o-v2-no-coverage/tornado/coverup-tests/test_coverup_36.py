# file: tornado/locale.py:428-448
# asked: {"lines": [428, 429, 436, 437, 438, 439, 440, 441, 442, 445, 446, 447], "branches": [[438, 439], [438, 445]]}
# gained: {"lines": [428, 429, 436, 437, 438, 439, 440, 441, 442, 445, 446, 447], "branches": [[438, 439], [438, 445]]}

import pytest
import datetime
from tornado.locale import Locale

@pytest.fixture
def locale(mocker):
    mocker.patch.object(Locale, 'translate', side_effect=lambda x, plural_message=None, count=None: x)
    return Locale("en_US")

def test_format_day_with_dow(locale, mocker):
    date = datetime.datetime(2023, 10, 5)  # Assume this is a Thursday
    formatted_day = locale.format_day(date, gmt_offset=0, dow=True)
    assert formatted_day == "Thursday, October 5"

def test_format_day_without_dow(locale, mocker):
    date = datetime.datetime(2023, 10, 5)  # Assume this is a Thursday
    formatted_day = locale.format_day(date, gmt_offset=0, dow=False)
    assert formatted_day == "October 5"

def test_format_day_with_gmt_offset(locale, mocker):
    date = datetime.datetime(2023, 10, 5, 12, 0)  # Assume this is a Thursday at noon
    formatted_day = locale.format_day(date, gmt_offset=60, dow=True)  # 1 hour offset
    assert formatted_day == "Thursday, October 5"
