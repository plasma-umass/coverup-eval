# file: pypara/dcc.py:574-597
# asked: {"lines": [574, 575, 597], "branches": []}
# gained: {"lines": [574, 575, 597], "branches": []}

import datetime
from decimal import Decimal
from pypara.dcc import dcfc_nl_365
from pypara.commons.zeitgeist import Date

def test_dcfc_nl_365_no_leap_year():
    start = Date(2007, 12, 28)
    asof = Date(2008, 2, 28)
    end = Date(2008, 2, 28)
    result = dcfc_nl_365(start, asof, end)
    assert round(result, 14) == Decimal('0.16986301369863')

def test_dcfc_nl_365_with_leap_year():
    start = Date(2007, 12, 28)
    asof = Date(2008, 2, 29)
    end = Date(2008, 2, 29)
    result = dcfc_nl_365(start, asof, end)
    assert round(result, 14) == Decimal('0.16986301369863')

def test_dcfc_nl_365_full_year():
    start = Date(2007, 10, 31)
    asof = Date(2008, 11, 30)
    end = Date(2008, 11, 30)
    result = dcfc_nl_365(start, asof, end)
    assert round(result, 14) == Decimal('1.08219178082192')

def test_dcfc_nl_365_more_than_year():
    start = Date(2008, 2, 1)
    asof = Date(2009, 5, 31)
    end = Date(2009, 5, 31)
    result = dcfc_nl_365(start, asof, end)
    assert round(result, 14) == Decimal('1.32602739726027')
