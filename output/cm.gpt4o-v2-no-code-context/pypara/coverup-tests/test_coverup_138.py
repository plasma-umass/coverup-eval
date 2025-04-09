# file: pypara/dcc.py:86-146
# asked: {"lines": [121, 124, 127, 130, 133, 136, 139, 142, 143, 146], "branches": [[142, 143], [142, 146]]}
# gained: {"lines": [121, 124, 127, 130, 133, 136, 139, 142, 143, 146], "branches": [[142, 143], [142, 146]]}

import datetime
from decimal import Decimal
from typing import Union, Optional
import pytest

# Assuming _last_payment_date and _construct_date are defined in pypara.dcc
from pypara.dcc import _last_payment_date, _construct_date

def test_last_payment_date_case1():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 12, 31)
    frequency = 1
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 1, 1)

def test_last_payment_date_case2():
    start = datetime.date(2015, 1, 1)
    asof = datetime.date(2015, 12, 31)
    frequency = 1
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 1, 1)

def test_last_payment_date_case3():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 12, 31)
    frequency = 2
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 7, 1)

def test_last_payment_date_case4():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 8, 31)
    frequency = 2
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 7, 1)

def test_last_payment_date_case5():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 4, 30)
    frequency = 2
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 1, 1)

def test_last_payment_date_case6():
    start = datetime.date(2014, 6, 1)
    asof = datetime.date(2015, 4, 30)
    frequency = 1
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2014, 6, 1)

def test_last_payment_date_case7():
    start = datetime.date(2008, 7, 7)
    asof = datetime.date(2015, 10, 6)
    frequency = 4
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 7, 7)

def test_last_payment_date_case8():
    start = datetime.date(2014, 12, 9)
    asof = datetime.date(2015, 12, 4)
    frequency = 1
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2014, 12, 9)

def test_last_payment_date_case9():
    start = datetime.date(2012, 12, 15)
    asof = datetime.date(2016, 1, 6)
    frequency = 2
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 12, 15)

def test_last_payment_date_case10():
    start = datetime.date(2012, 12, 15)
    asof = datetime.date(2015, 12, 31)
    frequency = 2
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 12, 15)

def test_last_payment_date_eom():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 12, 31)
    frequency = 1
    eom = 31
    result = _last_payment_date(start, asof, frequency, eom)
    assert result == datetime.date(2015, 1, 31)

def test_last_payment_date_invalid_date():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 12, 31)
    frequency = 1
    eom = -1
    result = _last_payment_date(start, asof, frequency, eom)
    assert result == start
