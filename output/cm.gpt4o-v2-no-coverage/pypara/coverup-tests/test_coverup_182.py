# file: pypara/dcc.py:86-146
# asked: {"lines": [121, 124, 127, 130, 133, 136, 139, 142, 143, 146], "branches": [[142, 143], [142, 146]]}
# gained: {"lines": [121, 124, 127, 130, 133, 136, 139, 142, 143, 146], "branches": [[142, 143], [142, 146]]}

import datetime
from decimal import Decimal
from typing import Optional, Union
import pytest
from pypara.dcc import _last_payment_date
from pypara.commons.zeitgeist import Date

def test_last_payment_date_case1():
    assert _last_payment_date(Date(2014, 1, 1), Date(2015, 12, 31), 1) == Date(2015, 1, 1)

def test_last_payment_date_case2():
    assert _last_payment_date(Date(2015, 1, 1), Date(2015, 12, 31), 1) == Date(2015, 1, 1)

def test_last_payment_date_case3():
    assert _last_payment_date(Date(2014, 1, 1), Date(2015, 12, 31), 2) == Date(2015, 7, 1)

def test_last_payment_date_case4():
    assert _last_payment_date(Date(2014, 1, 1), Date(2015, 8, 31), 2) == Date(2015, 7, 1)

def test_last_payment_date_case5():
    assert _last_payment_date(Date(2014, 1, 1), Date(2015, 4, 30), 2) == Date(2015, 1, 1)

def test_last_payment_date_case6():
    assert _last_payment_date(Date(2014, 6, 1), Date(2015, 4, 30), 1) == Date(2014, 6, 1)

def test_last_payment_date_case7():
    assert _last_payment_date(Date(2008, 7, 7), Date(2015, 10, 6), 4) == Date(2015, 7, 7)

def test_last_payment_date_case8():
    assert _last_payment_date(Date(2014, 12, 9), Date(2015, 12, 4), 1) == Date(2014, 12, 9)

def test_last_payment_date_case9():
    assert _last_payment_date(Date(2012, 12, 15), Date(2016, 1, 6), 2) == Date(2015, 12, 15)

def test_last_payment_date_case10():
    assert _last_payment_date(Date(2012, 12, 15), Date(2015, 12, 31), 2) == Date(2015, 12, 15)

def test_last_payment_date_eom():
    assert _last_payment_date(Date(2014, 1, 1), Date(2015, 12, 31), 1, 31) == Date(2015, 1, 31)

def test_last_payment_date_invalid_date():
    assert _last_payment_date(Date(2014, 1, 1), Date(2015, 12, 31), 1, -1) == Date(2014, 1, 1)
