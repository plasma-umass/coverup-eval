# file: tornado/locale.py:328-426
# asked: {"lines": [347, 348, 349, 350, 351, 355, 358, 359, 360, 361, 362, 363, 364, 366, 367, 368, 369, 370, 371, 372, 375, 376, 377, 378, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 397, 398, 399, 400, 401, 404, 405, 406, 407, 408, 409, 410, 411, 414, 415, 416, 417, 420, 421, 422, 423, 424, 425], "branches": [[347, 348], [347, 349], [350, 351], [350, 359], [351, 355], [351, 358], [368, 369], [368, 397], [369, 370], [369, 384], [370, 371], [370, 375], [375, 376], [375, 381], [384, 385], [384, 386], [386, 387], [386, 388], [388, 389], [388, 390], [390, 391], [390, 397], [397, 398], [397, 404], [405, 406], [405, 407], [407, 408], [407, 414]]}
# gained: {"lines": [347, 348, 349, 350, 351, 355, 358, 359, 360, 361, 362, 363, 364, 366, 367, 368, 369, 370, 371, 372, 375, 376, 377, 378, 381, 382, 384, 386, 387, 388, 389, 390, 391, 392, 393, 394, 397, 398, 399, 400, 401, 404, 405, 406, 407, 408, 409, 410, 411, 414, 415, 416, 417, 420, 421, 422, 423, 424, 425], "branches": [[347, 348], [347, 349], [350, 351], [350, 359], [351, 355], [351, 358], [368, 369], [368, 397], [369, 370], [369, 384], [370, 371], [370, 375], [375, 376], [375, 381], [384, 386], [386, 387], [386, 388], [388, 389], [388, 390], [390, 391], [390, 397], [397, 398], [397, 404], [405, 406], [405, 407], [407, 408], [407, 414]]}

import pytest
import datetime
from unittest.mock import Mock
from tornado.locale import Locale

@pytest.fixture
def locale():
    locale = Locale.__new__(Locale)
    locale.code = "en"
    locale.name = "English"
    locale.rtl = False
    locale.translate = Mock(side_effect=lambda s, p=None, c=None: s if c is None else p % {"seconds": c, "minutes": c, "hours": c})
    locale._months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    locale._weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return locale

def test_format_date_int_timestamp(locale):
    timestamp = 1609459200  # 2021-01-01 00:00:00 UTC
    result = locale.format_date(timestamp)
    assert "January 1, 2021" in result

def test_format_date_float_timestamp(locale):
    timestamp = 1609459200.0  # 2021-01-01 00:00:00 UTC
    result = locale.format_date(timestamp)
    assert "January 1, 2021" in result

def test_format_date_datetime(locale):
    date = datetime.datetime(2021, 1, 1, 0, 0, 0)
    result = locale.format_date(date)
    assert "January 1, 2021" in result

def test_format_date_future_relative(locale):
    future_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
    result = locale.format_date(future_date, relative=True)
    assert "1 second ago" in result or "seconds ago" in result

def test_format_date_future_full_format(locale):
    future_date = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    result = locale.format_date(future_date, full_format=True)
    assert "at" in result

def test_format_date_past_relative_seconds(locale):
    past_date = datetime.datetime.utcnow() - datetime.timedelta(seconds=30)
    result = locale.format_date(past_date, relative=True)
    assert "1 second ago" in result or "seconds ago" in result

def test_format_date_past_relative_minutes(locale):
    past_date = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
    result = locale.format_date(past_date, relative=True)
    assert "1 minute ago" in result or "minutes ago" in result

def test_format_date_past_relative_hours(locale):
    past_date = datetime.datetime.utcnow() - datetime.timedelta(hours=2)
    result = locale.format_date(past_date, relative=True)
    assert "1 hour ago" in result or "hours ago" in result

def test_format_date_past_yesterday(locale):
    past_date = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    result = locale.format_date(past_date, relative=True)
    assert "yesterday" in result

def test_format_date_past_days(locale):
    past_date = datetime.datetime.utcnow() - datetime.timedelta(days=3)
    result = locale.format_date(past_date, relative=True)
    assert "at" in result

def test_format_date_past_months(locale):
    past_date = datetime.datetime.utcnow() - datetime.timedelta(days=200)
    result = locale.format_date(past_date, relative=True)
    assert "at" in result

def test_format_date_past_year(locale):
    past_date = datetime.datetime.utcnow() - datetime.timedelta(days=400)
    result = locale.format_date(past_date, relative=True)
    assert "at" in result

def test_format_date_gmt_offset(locale):
    date = datetime.datetime(2021, 1, 1, 12, 0, 0)
    result = locale.format_date(date, gmt_offset=60)
    assert "11:00" in result

def test_format_date_shorter(locale):
    date = datetime.datetime(2021, 1, 1, 12, 0, 0)
    result = locale.format_date(date, shorter=True)
    assert "Jan" in result or "January" in result

def test_format_date_24_hour_clock(locale):
    locale.code = "fr"
    date = datetime.datetime(2021, 1, 1, 15, 0, 0)
    result = locale.format_date(date)
    assert "15:00" in result

def test_format_date_12_hour_clock(locale):
    locale.code = "en"
    date = datetime.datetime(2021, 1, 1, 15, 0, 0)
    result = locale.format_date(date)
    assert "3:00 pm" in result

def test_format_date_zh_CN(locale):
    locale.code = "zh_CN"
    date = datetime.datetime(2021, 1, 1, 15, 0, 0)
    result = locale.format_date(date)
    assert "下午3:00" in result
