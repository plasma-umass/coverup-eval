# file: pypara/dcc.py:399-440
# asked: {"lines": [399, 400, 424, 427, 430, 432, 434, 437, 440], "branches": [[430, 432], [430, 440], [432, 434], [432, 437]]}
# gained: {"lines": [399, 400, 424, 427, 430, 432, 434, 437, 440], "branches": [[430, 432], [430, 440], [432, 434], [432, 437]]}

import datetime
import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.dcc import dcfc_act_act

def test_dcfc_act_act_non_leap_year():
    start = Date(2007, 12, 28)
    asof = Date(2008, 2, 28)
    end = asof
    result = dcfc_act_act(start, asof, end)
    expected = Decimal('0.16942884946478')
    assert round(result, 14) == expected

def test_dcfc_act_act_leap_year():
    start = Date(2007, 12, 28)
    asof = Date(2008, 2, 29)
    end = asof
    result = dcfc_act_act(start, asof, end)
    expected = Decimal('0.17216108990194')
    assert round(result, 14) == expected

def test_dcfc_act_act_multiple_years():
    start = Date(2007, 10, 31)
    asof = Date(2008, 11, 30)
    end = asof
    result = dcfc_act_act(start, asof, end)
    expected = Decimal('1.08243131970956')
    assert round(result, 14) == expected

def test_dcfc_act_act_leap_and_non_leap_years():
    start = Date(2008, 2, 1)
    asof = Date(2009, 5, 31)
    end = asof
    result = dcfc_act_act(start, asof, end)
    expected = Decimal('1.32625945055768')
    assert round(result, 14) == expected
