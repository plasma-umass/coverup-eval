# file tornado/locale.py:428-448
# lines [428, 429, 436, 437, 438, 439, 440, 441, 442, 445, 446, 447]
# branches ['438->439', '438->445']

import datetime
import pytest
from tornado.locale import Locale

class MockLocale(Locale):
    def __init__(self, code):
        self.code = code
        self._translations = {}
        self._months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        self._weekdays = [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ]

    def translate(self, message, plural_message=None, count=None):
        return message

@pytest.fixture
def mock_locale():
    return MockLocale('en_US')

def test_format_day_with_dow(mock_locale):
    date = datetime.datetime(2023, 4, 1)  # April 1st, 2023 is a Saturday
    formatted_date = mock_locale.format_day(date)
    assert formatted_date == "Saturday, April 1"

def test_format_day_without_dow(mock_locale):
    date = datetime.datetime(2023, 4, 1)  # April 1st, 2023 is a Saturday
    formatted_date = mock_locale.format_day(date, dow=False)
    assert formatted_date == "April 1"
