# file: pypara/dcc.py:86-146
# asked: {"lines": [143], "branches": [[142, 143]]}
# gained: {"lines": [143], "branches": [[142, 143]]}

import datetime
import pytest
from pypara.dcc import _last_payment_date
from pypara.commons.zeitgeist import Date

def test_last_payment_date_edge_case():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 12, 31)
    frequency = 1
    eom = -1  # This should trigger the condition to return start
    result = _last_payment_date(start, asof, frequency, eom)
    assert result == start

def test_last_payment_date_normal_case():
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 12, 31)
    frequency = 1
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 1, 1)

def test_last_payment_date_another_case():
    start = datetime.date(2012, 12, 15)
    asof = datetime.date(2015, 12, 31)
    frequency = 2
    result = _last_payment_date(start, asof, frequency)
    assert result == datetime.date(2015, 12, 15)
