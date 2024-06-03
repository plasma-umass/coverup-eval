# file tornado/locale.py:428-448
# lines [428, 429, 436, 437, 438, 439, 440, 441, 442, 445, 446, 447]
# branches ['438->439', '438->445']

import datetime
import pytest
from unittest import mock

# Assuming the Locale class is part of the tornado.locale module
from tornado.locale import Locale

class TestLocale:
    @pytest.fixture
    def locale(self):
        class TestLocale(Locale):
            _months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            _weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
            def __init__(self, code):
                self.code = code

            def translate(self, text):
                return text

        return TestLocale("en")

    def test_format_day_with_dow(self, locale):
        date = datetime.datetime(2023, 1, 22)  # A Sunday
        formatted_date = locale.format_day(date, gmt_offset=0, dow=True)
        assert formatted_date == "Sunday, January 22"

    def test_format_day_without_dow(self, locale):
        date = datetime.datetime(2023, 1, 22)  # A Sunday
        formatted_date = locale.format_day(date, gmt_offset=0, dow=False)
        assert formatted_date == "January 22"

    def test_format_day_with_gmt_offset(self, locale):
        date = datetime.datetime(2023, 1, 22, 12, 0)  # A Sunday at noon
        formatted_date = locale.format_day(date, gmt_offset=60, dow=True)  # GMT+1
        assert formatted_date == "Sunday, January 22"

    def test_format_day_without_dow_with_gmt_offset(self, locale):
        date = datetime.datetime(2023, 1, 22, 12, 0)  # A Sunday at noon
        formatted_date = locale.format_day(date, gmt_offset=60, dow=False)  # GMT+1
        assert formatted_date == "January 22"
